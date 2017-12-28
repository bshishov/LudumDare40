## PROTOTYPE FOR REFACTORING
from typing import Dict, Optional
from game.rules import *
from game.states import *


class EffectContext(object):
    def __init__(self, g, action):
        self.game = g
        self.action = action

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class EffectHandler(object):
    effect = EffectType.APPLY_BUFF

    def apply(self,
              ctx: EffectContext,
              source_entity: Optional[EntityState],
              target_entity: EntityState,
              buff_name: str,
              buff_duration: Optional[int]=None):
        pass

    def __call__(self, *args, **kwargs):
        self.apply(*args, **kwargs)


class ApplyBuff(EffectHandler):
    pass


class EffectProcessor(object):
    handlers = {
        EffectType.APPLY_BUFF, ApplyBuff(),
        EffectType.DAMAGE, ApplyBuff(),
    }  # type: Dict[EffectType, EffectHandler]

    def apply(self, ctx: EffectContext, effect_type, *args, **kwargs):
        self.handlers.get(effect_type).apply(ctx, *args, **kwargs)
