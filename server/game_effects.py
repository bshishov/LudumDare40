from game import *


def collect_handler(handlers):
    def effect_handler(effect_type):
        def decorator(fn):
            def wrapper(self, entity, *args, **kwargs):
                fn(self, entity, *args, **kwargs)
                self.game.notify_players(MSG_SRV_GAME_EFFECT,
                                         status='effect',
                                         entity=entity.id,
                                         effect=effect_type,
                                         args=args,
                                         kwargs=kwargs)
            handlers[effect_type] = wrapper
            return wrapper

        return decorator

    return effect_handler


class EffectHandler(object):
    handlers = {}
    effect_handler = collect_handler(handlers)

    def __init__(self, game):
        self.game = game  # type: CardGame
        self.logger = logging.getLogger(self.__class__.__name__)

    def apply_effects(self, source_entity, effects):
        """
            @type source_entity: EntityState
            @type effects: List[Dict]
        """
        for effect in effects:
            e_range = effect.get(P_EFFECT_RANGE, 10)
            targets = self.game.get_targets(source_entity, effect.get(P_EFFECT_TARGET), e_range)
            for e in targets:
                # e type: Entity
                self._apply_effect(source_entity, e, effect)

    def _apply_effect(self, source_entity, entity, effect):
        ef_type = effect.get(P_EFFECT_TYPE, None)
        ef_value = effect.get(P_EFFECT_VALUE, None)
        ef_range_mod = effect.get(P_EFFECT_RANGE_MOD, 0)
        ef_range = effect.get(P_EFFECT_RANGE, None)

        # Modify effect value by range modifier
        if isinstance(ef_value, int) and isinstance(ef_range, int):
            ef_value = max(0, ef_value + ef_range_mod * (ef_range - abs(source_entity.position - entity.position)))

        if ef_type is None:
            raise GameError('Effect has no type: {0}'.format(effect))

        if ef_type not in self.handlers:
            raise GameError('No handler for effect: {0}'.format(ef_type))

        # TODO: PASS ARGUMENTS WISELY
        kwargs = effect.copy()
        del kwargs[P_EFFECT_TYPE]
        if P_EFFECT_VALUE in kwargs:
            del kwargs[P_EFFECT_VALUE]
        if P_EFFECT_TARGET in kwargs:
            del kwargs[P_EFFECT_TARGET]
        self.logger.debug('effect: {0} val: {1}'.format(ef_type, ef_value))
        self.handlers[ef_type](self, entity, ef_value, **kwargs)

    @effect_handler(EFFECT_TYPE_DAMAGE)
    def effect_damage(self, entity, amount):
        """
            @type entity: EntityState
            @type amount: int
        """
        damage = amount + entity.damage_mod
        self._entity_modify_hp(entity, -damage)

    @effect_handler(EFFECT_TYPE_EDAMAGE)
    def effect_edamage(self, entity, amount):
        self._entity_modify_energy(entity, -amount)

    @effect_handler(EFFECT_TYPE_HEAL)
    def effect_heal(self, entity, amount):
        self._entity_modify_hp(entity, amount)

    @effect_handler(EFFECT_TYPE_EHEAL)
    def effect_eheal(self, entity, amount):
        self._entity_modify_energy(entity, amount)

    @effect_handler(EFFECT_TYPE_APPLY_BUFF)
    def effect_apply_buff(self, entity, buff_name):
        if entity.buffable:
            buff = get_buff(buff_name)
            duration = buff.get(P_BUFF_DURATION)

            buff_state = entity.get_buff(buff_name)
            if buff_state is None:
                # If no such buff - apply new
                entity.buffs.append(BuffState(buff_name, duration))
                self.apply_effects(entity, buff.get(P_BUFF_ON_APPLY_EFFECTS, []))
            else:
                # If buff is not applied - update duration
                buff_state.duration = duration

    @effect_handler(EFFECT_TYPE_REMOVE_BUFF)
    def effect_remove_buff(self, entity, buff_name):
        """
            @type entity: EntityState
            @type buff_name: str
        """
        buff_state = entity.get_buff(buff_name)
        if buff_state is not None:
            buff = get_buff(buff_name)
            entity.buffs.remove(buff_state)
            self.apply_effects(buff.get(entity, P_BUFF_ON_REMOVE_EFFECTS, []))

    @effect_handler(EFFECT_TYPE_ADD_CARDCOST)
    def effect_add_card_cost(self, entity, amount, card_type):
        self._change_card_cost(entity, card_type, amount)

    @effect_handler(EFFECT_TYPE_REDUCE_CARDCOST)
    def effect_add_card_cost(self, entity, amount, card_type):
        self._change_card_cost(entity, card_type, -amount)

    @effect_handler(EFFECT_TYPE_MOVE)
    def effect_move(self, entity, amount):
        """
            @type entity: EntityState
            @type amount: int
        """
        if entity.locked:
            self.logger.debug('Entity is locked, cannot move: {0}'.format(entity.name))
            return

        new_pos = entity.position + amount

        if self.game.is_player(entity):
            enemy = self.game.get_enemy_ship(entity)
            # Side check to perform swap without recursion
            if enemy.position == new_pos and enemy.side == SIDE_A:
                if enemy.locked:
                    self.logger.debug('Trying to move locked players')
                else:
                    self.effect_move(enemy, -amount)
                    self.game.invoke_case(enemy, CASE_COLLIDE, new_pos)
                    self.game.invoke_case(entity, CASE_COLLIDE, new_pos)
        else:
            if new_pos not in range(self.game.board_size):
                self.effect_destroy(entity)
                return

        new_pos = max(min(new_pos, self.game.board_size - 1), 0)
        entity.position = new_pos

        es = self.game.get_entities_at(new_pos)
        if len(es) > 1:
            for e in es:
                self.game.invoke_case(e, CASE_COLLIDE, entity.position)

    @effect_handler(EFFECT_TYPE_DISARM)
    def effect_disarm(self, entity):
        entity.armed = False

    @effect_handler(EFFECT_TYPE_ARM)
    def effect_arm(self, entity):
        entity.armed = True

    @effect_handler(EFFECT_TYPE_MUTE)
    def effect_mute(self, entity):
        entity.muted = True

    @effect_handler(EFFECT_TYPE_UNMUTE)
    def effect_unmute(self, entity):
        entity.muted = False

    @effect_handler(EFFECT_TYPE_LOCK_POSITION)
    def effect_lock_position(self, entity):
        entity.locked = True

    @effect_handler(EFFECT_TYPE_UNLOCK_POSITION)
    def effect_unlock_position(self, entity):
        entity.locked = False

    @effect_handler(EFFECT_TYPE_SPAWN)
    def effect_spawn(self, entity, name, spawn_position):
        if name not in objects:
            raise GameError('No such entity: {0}'.format(name))
        e = EntityState()
        e.name = name
        e.side = entity.side
        e.position = max(min(entity.position + spawn_position, self.game.board_size - 1), 0)
        self.game._last_entity_id += 1
        e.id = self.game._last_entity_id
        self.game.objects.append(e)

    @effect_handler(EFFECT_TYPE_DESTROY)
    def effect_destroy(self, entity):
        if self.game.is_player(entity):
            raise GameError('Player entity can not be destroyed: {0}'.format(entity.id), crucial=False)
        self.game.objects.remove(entity)
        self.game.invoke_case(entity, CASE_DESTROYED, entity.name)

    @effect_handler(EFFECT_TYPE_DAMAGE_ADD)
    def effect_damage_add(self, entity, amount):
        entity.damage_mod += amount

    @effect_handler(EFFECT_TYPE_DAMAGE_REDUCE)
    def effect_damage_reduce(self, entity, amount):
        entity.damage_mod -= amount

    @effect_handler(EFFECT_TYPE_ENERGYGAIN_ADD)
    def effect_egain_add(self, entity, amount):
        entity.energy_gain += amount

    @effect_handler(EFFECT_TYPE_ENERGYGAIN_REDUCE)
    def effect_egain_reduce(self, entity, amount):
        entity.energy_gain += max(entity.energy_gain - amount, 0)

    @effect_handler(EFFECT_TYPE_DRAW_CARD)
    def effect_draw_card(self, entity):
        """
            @type entity: EntityState
        """
        if not self.game.is_player(entity):
            raise GameError('Non-player entities cannot draw card')
        if isinstance(entity, PlayerState):
            if len(entity.deck) > 0:
                card = random.sample(entity.deck, 1)[0]
                entity.deck.remove(card)
                self.effect_gain_card(entity, card)
                return

    @effect_handler(EFFECT_TYPE_DROP_CARD_OF_TYPE)
    def effect_drop_card(self, entity):
        """
            @type entity: EntityState
        """
        if not self.game.is_player(entity):
            raise GameError('Non-player entities cannot have cards: {0}'.format(entity.name), crucial=False)
        if isinstance(entity, PlayerState):
            if len(entity.hand) > 0:
                card_to_drop = random.sample(entity.hand, 1)[0]
                entity.hand.remove(card_to_drop)
                self.game.invoke_case(entity, CASE_DROP_CARD, card_to_drop)

    @effect_handler(EFFECT_TYPE_GAIN_CARD)
    def effect_gain_card(self, entity, card_name):
        """
            @type entity: PlayerState
            @type card_name: str
        """
        if not entity.is_player:
            raise GameError('Only players can gain cards: {0}'.format(entity.get_state()), crucial=False)

        if card_name not in cards:
            raise GameError('Now such card: {0}'.format(card_name))

        entity.hand.append(CardState(card_name))

    @effect_handler(EFFECT_TYPE_REMOVE_CARD)
    def effect_remove_card(self, entity, card_name):
        """
            @type entity: PlayerState
            @type card_name: str
        """
        if not entity.is_player:
            raise GameError('Only players can gain cards: {0}'.format(entity.get_state()), crucial=False)

        if card_name not in cards:
            raise GameError('Now such card: {0}'.format(card_name))

        for card_state in entity.hand:
            if card_state.name == card_name:
                entity.hand.remove(card_state)

    @effect_handler(EFFECT_TYPE_ENERGY_TEST)
    def effect_energy_test(self, entity, threshold):
        if entity.energy >= threshold:
            self.effect_edamage(entity, threshold)
        else:
            self.effect_damage(entity, threshold - entity.energy)
            self.effect_edamage(entity, threshold)

    @effect_handler(EFFECT_TYPE_SPECIAL_SWAP)
    def effect_energy_test(self, entity):
        enemy = self.game.get_enemy_ship(entity)
        pos = entity.position
        self.effect_move(entity, -1)
        self.effect_move(enemy, pos - enemy.position)

    @effect_handler(EFFECT_TYPE_OFFENSE_APPROACH)
    def effect_energy_test(self, entity):
        enemy = self.game.get_enemy_ship(entity)
        if self.game.is_offense(entity):
            self.effect_move(entity, enemy.position - entity.position - 1)
        else:
            self.effect_move(enemy, entity.position - enemy.position - 1)

    def _change_card_cost(self, entity, card_type, amount):
        """
            @type entity: EntityState
            @type card_type: str
            @type amount: int
        """
        if not isinstance(entity, PlayerState):
            raise GameError('Non-player entities does not have cards: {0}'.format(card_type), crucial=False)
        for card_state in entity.hand:
            card_state.cost_defense += amount
            card_state.cost_offense += amount

    def _entity_modify_hp(self, entity, amount):
        entity.hp += amount
        entity.hp = max(entity.hp, 0)
        if entity.hp == 0:
            if not self.game.is_player(entity):
                self.effect_destroy(entity)
            else:
                self.game.end()

    def _entity_modify_energy(self, entity, amount):
        """
            @type entity: EntityState
            @type amount: int
        """
        entity.energy += amount
        entity.energy = max(entity.energy, 0)
