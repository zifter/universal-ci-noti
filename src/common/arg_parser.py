from argparse import ArgumentParser
from .logger import g_logger


def _cast_bool(s: str):
    return s.lower() in {'1', 'true'}


class ArgParser(ArgumentParser):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)

    def add_bool_argument(self, *args, **kwargs):
        kwargs['type'] = _cast_bool
        self.add_argument(*args, **kwargs)

    def parse_args(self, *args, **kwargs):
        args = super().parse_args()
        g_logger.info(args)
        return args

    def __repr__(self):
        return 'ArgParser'
