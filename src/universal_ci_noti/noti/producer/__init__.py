import abc

from universal_ci_noti.noti.queue import NotificationQueue


class NotificationProducer:
    def __init__(self, queue: NotificationQueue):
        self.queue: NotificationQueue = queue

    @abc.abstractmethod
    async def go(self):
        raise NotImplementedError()

    @abc.abstractmethod
    async def exit(self):
        raise NotImplementedError()
