from typing import List, Tuple, Callable, Dict, Optional
import logging
import random

from framework.game import GameError
import network.protocol_tools as proto
from game.rules import *
from game.states import *


__all__ = ['EffectHandler', ]


def collect_handler(handlers: Dict[EffectType, Tuple[Callable, Tuple]]):
    def effect_handler(effect_type: EffectType, *args_def):
        def decorator(fn: Callable[['EffectHandler', EntityState, EntityState], None]):
            def wrapper(self: 'EffectHandler', source_entity: EntityState, target_entity: EntityState, *args, **kwargs):
                if source_entity is None:
                    source_id = None
                else:
                    source_id = source_entity.id

                self.logger.debug('Applying effect [{0}] from entity {1} to entity:{2} {3} {4}'.format(
                    effect_type, source_id, target_entity.id, args, kwargs))

                # Apply effect
                fn(self, source_entity, target_entity, *args, **kwargs)

                message = self.game.create_message(
                    head=proto.Head.SRV_GAME_EFFECT,
                    status='effect')  # type: proto.Message

                ef = message.game.effect
                if source_entity is not None:
                    ef.source_entity = source_entity.id
                ef.target_entity = target_entity.id
                ef.effect_name = effect_type.value
                for arg, arg_def in zip(args, args_def):
                    arg_name, _ = arg_def  # type: Tuple[EffectType, obj]
                    a = proto.GameEffectArgument()
                    a.key = str(arg_name.value)
                    a.value = str(arg)
                    ef.arguments.append(a)

                # Notify players about the effect
                self.game.send_players(message)

            handlers[effect_type] = (wrapper, args_def)
            return wrapper

        return decorator

    return effect_handler


class EffectHandler(object):
    handlers = {}
    effect_handler = collect_handler(handlers)

    def __init__(self, g: 'game.card_game.CardGame'):
        self.game = g  # type: game.card_game.CardGame
        self.logger = logging.getLogger(self.__class__.__name__)

    def apply_effects(self, source_entity: EntityState, effects: List[Dict]):
        for effect in effects:
            e_range = effect.get(Effect.RANGE, 10)
            targets = self.game.get_targets(source_entity, effect.get(Effect.TARGET), e_range)
            for e in targets:
                self._apply_effect(source_entity, e, effect)

    def _apply_effect(self, source_entity: EntityState, target_entity: EntityState, effect: Dict):
        ef_type = effect.get(Effect.TYPE, None)

        if ef_type is None:
            raise GameError('Effect has no type: {0}'.format(effect))

        if ef_type not in self.handlers:
            raise GameError('No handler for effect: {0}'.format(ef_type))

        handler, args_def = self.handlers[ef_type]
        args = tuple([effect.get(ef_prop, ef_default) for ef_prop, ef_default in args_def])
        handler(self, source_entity, target_entity, *args)

    @effect_handler(EffectType.DAMAGE, (Effect.VALUE, 0), (Effect.RANGE, 10), (Effect.RANGE_MOD, 0))
    def damage(self,
               source_entity: Optional[EntityState],
               target_entity: EntityState,
               amount: int,
               ef_range: int=10,
               range_mod: int=0):
        dmg_source_mod = 0
        if source_entity is not None:
            dmg_source_mod = source_entity.damage_mod

        dmg_range_mod = range_mod * (ef_range - abs(source_entity.position - target_entity.position))
        damage = max(0, amount + dmg_source_mod + dmg_range_mod)
        self._entity_modify_hp(source_entity, target_entity, -damage)

    @effect_handler(EffectType.EDAMAGE, (Effect.VALUE, 0))
    def energy_damage(self, source_entity: Optional[EntityState], target_entity: EntityState, amount: int):
        self._entity_modify_energy(target_entity, -amount)

    @effect_handler(EffectType.HEAL, (Effect.VALUE, 0))
    def heal(self, source_entity: Optional[EntityState], target_entity: EntityState, amount: int):
        self._entity_modify_hp(source_entity, target_entity, amount)

    @effect_handler(EffectType.EHEAL, (Effect.VALUE, 0))
    def energy_heal(self, source_entity: Optional[EntityState], target_entity: EntityState, amount: int):
        self._entity_modify_energy(target_entity, amount)

    @effect_handler(EffectType.APPLY_BUFF, (Effect.VALUE, None), (Effect.BUFF_DURATION, None))
    def apply_buff(self, source_entity: Optional[EntityState], target_entity: EntityState,
                   buff_name: str, buff_duration: Optional[int]=None):
        if target_entity.buffable:
            buff = get_buff(buff_name)
            if buff_duration is None:
                duration = buff.get(Buff.DURATION)
            else:
                duration = buff_duration
            buff_state = target_entity.get_buff(buff_name)
            if buff_state is None:
                # If no such buff - apply new
                target_entity.buffs.append(BuffState(buff_name, duration))
                self.apply_effects(target_entity, buff.get(Buff.ON_APPLY_EFFECTS, []))
            else:
                # If buff is not applied - update duration
                buff_state.duration = duration

    @effect_handler(EffectType.REMOVE_BUFF, (Effect.VALUE, None))
    def remove_buff(self, source_entity: Optional[EntityState], target_entity: EntityState, buff_name: str):
        buff_state = target_entity.get_buff(buff_name)
        if buff_state is not None:
            buff = get_buff(buff_name)
            target_entity.buffs.remove(buff_state)
            self.apply_effects(target_entity, buff.get(Buff.ON_REMOVE_EFFECTS, []))

    @effect_handler(EffectType.ADD_CARDCOST, (Effect.VALUE, 0), (Effect.CARD_TYPE, None))
    def add_card_cost(self, source_entity: Optional[EntityState], target_entity: EntityState,
                      amount: int, card_type: str):
        self._change_card_cost(target_entity, card_type, amount)

    @effect_handler(EffectType.REDUCE_CARDCOST, (Effect.VALUE, 0), (Effect.CARD_TYPE, None))
    def reduce_card_cost(self, source_entity: Optional[EntityState], target_entity: EntityState,
                         amount: int, card_type: str):
        self._change_card_cost(target_entity, card_type, -amount)

    @effect_handler(EffectType.MOVE, (Effect.VALUE, 0))
    def move(self, source_entity: Optional[EntityState], target_entity: EntityState, amount: int):
        if target_entity.locked:
            self.logger.debug('Entity is locked, cannot move: {0}'.format(target_entity.name))
            return

        new_pos = target_entity.position + amount

        if new_pos not in range(self.game.board_size):
            if self.game.is_player(target_entity):
                # TODO: Add damage when out of the field
                pass
            else:
                self.destroy(source_entity, target_entity)
                return

            # Clamp new_pos
            new_pos = max(min(new_pos, self.game.board_size - 1), 0)

            # If position is not changed
            if new_pos == target_entity.position:
                return

        if self.game.is_player(target_entity):
            enemy = self.game.get_enemy_ship(target_entity)
            if enemy.position == new_pos:
                if enemy.locked:
                    self.logger.debug('Trying to move locked players')
                    return
                else:
                    # Move yourself first, then opponent
                    target_entity.position = new_pos

                    # Current move effect target as a source of enemy movement
                    self.move(target_entity, enemy, -amount)

                    # Raise collision cases
                    self.game.invoke_case(enemy, Case.COLLIDE, target_entity.name)
                    self.game.invoke_case(target_entity, Case.COLLIDE, enemy.name)

        target_entity.position = new_pos

        es = self.game.get_entities_at(new_pos)
        if len(es) > 1:
            for e in es:
                self.game.invoke_case(e, Case.COLLIDE, target_entity.name)

    @effect_handler(EffectType.DISARM)
    def disarm(self, source_entity: Optional[EntityState], target_entity: EntityState):
        target_entity.armed = False

    @effect_handler(EffectType.ARM)
    def arm(self, source_entity: Optional[EntityState], target_entity: EntityState):
        target_entity.armed = True

    @effect_handler(EffectType.MUTE)
    def mute(self, source_entity: Optional[EntityState], target_entity: EntityState):
        target_entity.muted = True

    @effect_handler(EffectType.UNMUTE)
    def un_mute(self, source_entity: Optional[EntityState], target_entity: EntityState):
        target_entity.muted = False

    @effect_handler(EffectType.LOCK_POSITION)
    def lock_position(self, source_entity: Optional[EntityState], target_entity: EntityState):
        target_entity.locked = True

    @effect_handler(EffectType.UNLOCK_POSITION)
    def unlock_position(self, source_entity: Optional[EntityState], target_entity: EntityState):
        target_entity.locked = False

    @effect_handler(EffectType.SPAWN, (Effect.VALUE, None), (Effect.SPAWN_POSITION, 0))
    def spawn(self, source_entity: Optional[EntityState], target_entity: EntityState, name: str, spawn_position: int):
        if name not in objects:
            raise GameError('No such entity: {0}'.format(name))
        e = EntityState()
        e.hp = objects[name].get(Entity.HP, e.hp)
        e.name = name
        e.side = target_entity.side
        e.position = max(min(target_entity.position + spawn_position, self.game.board_size - 1), 0)
        self.game._last_entity_id += 1
        e.id = self.game._last_entity_id
        self.game.objects.append(e)
        self.game.invoke_case(e, Case.SPAWNED, None)

    @effect_handler(EffectType.DESTROY)
    def destroy(self, source_entity: Optional[EntityState], target_entity: EntityState):
        if self.game.is_player(target_entity):
            raise GameError('Player entity can not be destroyed: {0}'.format(target_entity.id), crucial=False)
        self.game.objects.remove(target_entity)
        self.game.invoke_case(target_entity, Case.DESTROYED, target_entity.name)

    @effect_handler(EffectType.DAMAGE_ADD, (Effect.VALUE, 0))
    def damage_mod_add(self, source_entity: Optional[EntityState], target_entity: EntityState, amount: int):
        target_entity.damage_mod += amount

    @effect_handler(EffectType.DAMAGE_REDUCE, (Effect.VALUE, 0))
    def damage_mod_reduce(self, source_entity: Optional[EntityState], target_entity: EntityState, amount: int):
        target_entity.damage_mod -= amount

    @effect_handler(EffectType.ENERGYGAIN_ADD, (Effect.VALUE, 0))
    def energy_gain_add(self, source_entity: Optional[EntityState], target_entity: EntityState, amount: int):
        target_entity.energy_gain += amount

    @effect_handler(EffectType.ENERGYGAIN_REDUCE, (Effect.VALUE, 0))
    def energy_gain_reduce(self, source_entity: Optional[EntityState], target_entity: EntityState, amount: int):
        target_entity.energy_gain += max(target_entity.energy_gain - amount, 0)

    @effect_handler(EffectType.DRAW_CARD)
    def draw_card(self, source_entity: Optional[EntityState], target_entity: EntityState):
        if not self.game.is_player(target_entity):
            raise GameError('Non-player entities cannot draw card')
        if isinstance(target_entity, PlayerEntityState):
            if len(target_entity.deck) > 0:
                card = random.sample(target_entity.deck, 1)[0]
                target_entity.deck.remove(card)
                self.gain_card(source_entity, target_entity, card)

    @effect_handler(EffectType.DROP_CARD_OF_TYPE, (Effect.VALUE, None))
    def drop_card(self, source_entity: Optional[EntityState], target_entity: EntityState, card_type: str):
        if not self.game.is_player(target_entity):
            raise GameError('Non-player entities cannot have cards: {0}'.format(target_entity.name), crucial=False)

        '''
        if isinstance(target_entity, PlayerState):
            if len(target_entity.hand) > 0:
                card_to_drop = random.sample(target_entity.hand, 1)[0]
                target_entity.hand.remove(card_to_drop)
                self.game.invoke_case(target_entity, Case.DROP_CARD, card_to_drop)
        '''
        raise NotImplementedError()

    @effect_handler(EffectType.GAIN_CARD, (Effect.VALUE, None))
    def gain_card(self, source_entity: Optional[EntityState], target_entity: PlayerEntityState, card_name: str):
        if not target_entity.is_player:
            raise GameError('Only players can gain cards: {0}'.format(target_entity.get_state()), crucial=False)

        if card_name not in cards:
            raise GameError('Now such card: {0}'.format(card_name))

        target_entity.hand.append(CardState(card_name))

    @effect_handler(EffectType.REMOVE_CARD, (Effect.VALUE, None))
    def remove_card(self, source_entity: Optional[EntityState], target_entity: PlayerEntityState, card_name: str):
        if not target_entity.is_player:
            raise GameError('Only players can gain cards: {0}'.format(target_entity.get_state()), crucial=False)

        if card_name not in cards:
            raise GameError('Now such card: {0}'.format(card_name))

        for card_state in target_entity.hand:
            if card_state.name == card_name:
                target_entity.hand.remove(card_state)

    @effect_handler(EffectType.ENERGY_TEST, (Effect.VALUE, 0))
    def energy_test(self, source_entity: Optional[EntityState], target_entity: EntityState, threshold: int):
        if target_entity.energy >= threshold:
            self.energy_damage(source_entity, target_entity, threshold)
        else:
            self.damage(source_entity, target_entity, threshold - target_entity.energy)
            self.energy_damage(source_entity, target_entity, threshold)

    @effect_handler(EffectType.SPECIAL_SWAP)
    def special_swap(self, source_entity: Optional[EntityState], target_entity: EntityState):
        enemy = self.game.get_enemy_ship(target_entity)
        pos = target_entity.position
        self.move(source_entity, target_entity, -1)
        self.move(source_entity, enemy, pos - enemy.position)

    @effect_handler(EffectType.OFFENSE_APPROACH)
    def offense_approach(self, source_entity: Optional[EntityState], target_entity: EntityState):
        enemy = self.game.get_enemy_ship(target_entity)
        if self.game.is_offense(target_entity):
            self.move(source_entity, target_entity, enemy.position - target_entity.position - 1)
        else:
            self.move(source_entity, enemy, target_entity.position - enemy.position - 1)

    def _change_card_cost(self, entity: EntityState, card_type: str, amount: int):
        if not isinstance(entity, PlayerEntityState):
            raise GameError('Non-player entities does not have cards: {0}'.format(card_type), crucial=False)
        for card_state in entity.hand:
            c = get_card(card_state.name)
            if c.get(Card.TYPE, None) == card_type:
                card_state.cost_defense = max(card_state.cost_defense + amount, 0)
                card_state.cost_offense = max(card_state.cost_offense + amount, 0)

    def _entity_modify_hp(self, source_entity: Optional[EntityState], target_entity: EntityState, amount: int):
        target_entity.hp += amount
        target_entity.hp = max(target_entity.hp, 0)
        if target_entity.hp == 0:
            if not self.game.is_player(target_entity):
                self.destroy(source_entity, target_entity)
            else:
                self.game.end()

    def _entity_modify_energy(self, entity: EntityState, amount: int):
        entity.energy += amount
        entity.energy = max(entity.energy, 0)
