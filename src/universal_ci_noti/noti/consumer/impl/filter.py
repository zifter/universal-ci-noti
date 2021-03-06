from typing import List

from universal_ci_noti.noti.consumer import NotificationConsumer
from universal_ci_noti.noti.types import JobResult


class EventFilter:
    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return f"Filter[{self._name}]"

    async def filter(self) -> bool:
        """
        Filter before all events

        :return: True if event should be filtered out
        """
        return False

    async def filter_job_finished(self, _: JobResult) -> bool:
        """
        Check if job result should be filtered out

        :return: True if event should be filtered out
        """
        return False


class FilterConsumer(NotificationConsumer):
    def __init__(
        self, filters: List[EventFilter], initial_consumer: NotificationConsumer
    ):
        super().__init__()
        self._filters: List[EventFilter] = filters
        self._consumer: NotificationConsumer = initial_consumer

    def __repr__(self):
        return f"FilterConsumer{self._filters}"

    async def on_job_finished(self, job_result: JobResult):
        if any([await f.filter() for f in self._filters]):
            return

        if any([await f.filter_job_finished(job_result) for f in self._filters]):
            return

        await self._consumer.on_job_finished(job_result)
