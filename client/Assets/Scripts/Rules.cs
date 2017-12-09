using System;
namespace Assets.Scripts
{
    public static class Rules
    {
        public static string SideA = "a";
        public static string SideB = "b";

        // NOTE: These values MUST match /server/game/rules/settings.py

        // DB section
        public static string SectionShips = "ships";
        public static string SectionBuffs = "buffs";
        public static string SectionWeapons = "weapons";
        public static string SectionCards = "cards";
        public static string SectionObjects = "objects";

        // Common
        public static string PType = "type";
        public static string PValue = "value";
        public static string PTarget = "target";

        // Actions
        public static string ActionPlayCard = "play_card";
        public static string ActionFireWeapon = "fire_weapon";
        public static string ActionEndTurn = "end_turn";

        public static string TargetSelf = "self";

        // All
        public static string TargetAll = "all";
        public static string TargetAllExceptSelf = "all_except";
        public static string TargetAllEnemies = "all_enemies";
        public static string TargetAllAllies = "all_allies";
        public static string TargetAllShips = "all_ships";

        // Separate ships and objects
        public static string TargetEnemyShip = "enemy_ship";
        public static string TargetAllyShip = "ally_ship";

        // Special
        public static string TargetMaxHealth = "max_health";
        public static string TargetMinHealth = "min_health";
        public static string TargetMaxEnergy = "max_energy";

        // Directional
        public static string TargetForward = "forward";
        public static string TargetForwardAlly = "forward_ally";
        public static string TargetForwardEnemy = "forward_enemy";
        public static string TargetForwardPierce = "forward_pierce";
        public static string TargetBackward = "backward";
        public static string TargetBackwardAlly = "backward_ally";
        public static string TargetBackwardEnemy = "backward_enemy";
        public static string TargetBackwardPierce = "backward_pierce";

        // EFFECTS
        public static string EffectTypeDamage = "damage";
        public static string EffectTypeEdamage = "edamage";
        public static string EffectTypeHeal = "heal";
        public static string EffectTypeEheal = "eheal";
        public static string EffectTypeMove = "position";
        public static string EffectTypeDisarm = "disarm";
        public static string EffectTypeArm = "arm";
        public static string EffectTypeMute = "mute";
        public static string EffectTypeUnmute = "unmute";
        public static string EffectTypeLockPosition = "lock_position";
        public static string EffectTypeUnlockPosition = "unlock_position";
        public static string EffectTypeReduceCardcost = "reduce_cardcost";
        public static string EffectTypeAddCardcost = "add_cardcost";
        public static string EffectTypeDrawCard = "draw_card";
        public static string EffectTypeDropCardOfType = "drop_card";
        public static string EffectTypeRemoveCard = "remove_card";
        public static string EffectTypeGainCard = "gain_card";
        public static string EffectTypeDamageReduce = "damage_reduce";
        public static string EffectTypeDamageAdd = "damage_add";
        public static string EffectTypeEnergygainReduce = "energygain_reduce";
        public static string EffectTypeEnergygainAdd = "energygain_add";
        public static string EffectTypeSpawn = "spawn";
        public static string EffectTypeDestroy = "destroy";
        public static string EffectTypeApplyBuff = "apply_buff";
        public static string EffectTypeRemoveBuff = "remove_buff";
        public static string EffectTypeEnergyTest = "energy_test";

        // Speacial effects
        public static string EffectTypeSpecialSwap = "special_swap";
        public static string EffectTypeOffenseApproach = "approach";

        // Effect properties
        public static string PEffectType = PType;
        public static string PEffectValue = PValue;
        public static string PEffectTarget = PTarget;
        public static string PEffectRange = "range";
        public static string PEffectRangeMod = "range_mod";
        public static string PEffectSpawnPosition = "spawn_position";
        public static string PEffectCardType = "card_type";
        public static string PEffectBuffDuration = "buff_duration";

        // Cases
        public static string CaseCollide = "collide";
        public static string CaseDrawCard = "draw_card";
        public static string CasePlayCard = "play_card";
        public static string CaseDropCard = "drop_card";
        public static string CaseDestroyed = "entity_destroyed";
        public static string CaseOverload = "entity_overload";
        public static string CaseRoundEnd = "turn_end";
        public static string CaseRoundStart = "turn_start";

        // Event properties
        public static string PCaseArg = "arg";
        public static string PCaseEffects = "effects";

        // Ship properties
        public static string PShipHp = "hp";
        public static string PShipMaxEnergy = "max_energy";
        public static string PShipEnergyPerTurn = "energy_per_turn";
        public static string PShipCards = "cards";

        // Weapon properties
        public static string PWeaponDescription = "description";
        public static string PWeaponFullName = "full_name";
        public static string PWeaponCost = "cost";
        public static string PWeaponEffect = "effect";
        public static string PWeaponCards = "cards";
        public static string PWeaponActionOffense = "offense";
        public static string PWeaponActionDefense = "defense";
        public static string PWeaponActionSame = "same";
        public static string PWeaponTarget = PTarget;
        public static string PWeaponEffects = "effects";

        // Entities properties
        public static string PObjectFullName = "full_name";
        public static string PObjectDescription = "description";
        public static string PObjectCases = "cases";

        // Buff properties
        public static string PBuffFullName = "full_name";
        public static string PBuffDescription = "description";
        public static string PBuffDuration = "duration";
        public static string PBuffOnRoundEffects = "turn_effects";
        public static string PBuffOnApplyEffects = "apply_effects";
        public static string PBuffOnRemoveEffects = "remove_effects";
        public static string PBuffCases = "cases";

        // Card type
        public static string CardTypeEvent = "event";
        public static string CardTypeShip = "ship";
        public static string CardTypeWeapon = "weapon";

        // Card properties
        public static string PCardActionOffense = "offense";
        public static string PCardActionDefense = "defense";
        public static string PCardActionSame = "same";
        public static string PCardDeck = "deck";
        public static string PCardType = PType;
        public static string PCardCost = "cost";
        public static string PCardFullName = "full_name";
        public static string PCardDescription = "description";
        public static string PCardFlavor = "flavor";
        public static string PCardEffects = "effects";
    }
}
