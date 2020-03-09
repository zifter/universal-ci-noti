import time


class ElapsedTime:
    def __init__(self):
        self.start = time.time()

    @property
    def diff(self):
        return time.time() - self.start
