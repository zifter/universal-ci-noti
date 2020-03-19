import abc
import datetime
import logging

from universal_ci_noti.noti.consumer.impl.filter import EventFilter

logger = logging.getLogger("universal_ci_noti.noti.consumer.impl.working_hours_filter")


class WorkingHoursProvider:
    @abc.abstractmethod
    async def is_working_hours(self, dt: datetime.datetime) -> bool:
        """
        Return True if now is working hours, otherwise False
        """

    @abc.abstractmethod
    async def is_weekend(self, dt: datetime.date) -> bool:
        """
        Return True if today is weekend, otherwise False
        """

    @abc.abstractmethod
    async def is_holiday(self, dt: datetime.date) -> bool:
        """
        Return True if today is holiday, otherwise False
        """


class WorkingHoursFilter(EventFilter):
    def __init__(self, provider: WorkingHoursProvider):
        super().__init__("working_hours_filter")

        self._provider: WorkingHoursProvider = provider

    def now(self) -> datetime.datetime:
        return datetime.datetime.now()

    async def filter(self) -> bool:
        t = self.now()
        if await self._provider.is_holiday(t):
            logger.debug('Skip because today is holiday')
            return True

        if await self._provider.is_weekend(t):
            logger.debug('Skip because today is weekend')
            return True

        if not await self._provider.is_working_hours(t):
            logger.debug("Skip because now are not a working hours")
            return True

        return False
