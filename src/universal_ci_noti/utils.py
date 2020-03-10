import time
from multiprocessing import current_process
from threading import current_thread


class ElapsedTime:
    def __init__(self):
        self.start = time.time()

    @property
    def diff(self):
        return time.time() - self.start


def is_main_process() -> bool:
    return current_process().name == "MainProcess"


def is_main_thread() -> bool:
    return current_thread().name == "MainThread"
