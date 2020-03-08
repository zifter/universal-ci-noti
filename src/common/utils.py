import random
import string
import time
from collections import OrderedDict


class ElapsedTime:
    def __init__(self):
        self.start = time.time()

    @property
    def diff(self):
        return time.time() - self.start


def lookup_dict_attr(obj, attr):
    for obj in [obj] + obj.__class__.mro():
        if attr in obj.__dict__:
            return obj.__dict__[attr]
    raise AttributeError


def get_ordered_members(instance):
    return OrderedDict(instance.__dict__).items()


def random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
