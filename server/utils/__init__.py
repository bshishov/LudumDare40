import threading
from enum import Enum

__all__ = ['EventSubscription', 'unroll_enum_dict', 'set_interval']


class EventSubscription(list):
    """Event subscription.

    A list of callable objects. Calling an instance of this will cause a
    call to each item in the list in ascending order by index.

    """

    def __call__(self, *args, **kwargs):
        for f in self:
            f(*args, **kwargs)

    def __repr__(self):
        return "Event(%s)" % list.__repr__(self)


def set_interval(delay, fn, *args, **kwargs):
    if fn is None:
        return
    timer = threading.Timer(delay, fn, args=args, kwargs=kwargs)
    timer.start()
    return timer


def unroll_enum_dict(o):
    if isinstance(o, dict):
        out = {}
        for k in o:
            out[unroll_enum_dict(k)] = unroll_enum_dict(o[k])
        return out
    elif isinstance(o, list):
        out = []
        for v in o:
            out.append(unroll_enum_dict(v))
        return out
    elif isinstance(o, Enum):
        return o.value
    elif isinstance(o, (str, int, float)):
        return o
    raise RuntimeError('Can\'t convert type of object {0}'.format(o))
