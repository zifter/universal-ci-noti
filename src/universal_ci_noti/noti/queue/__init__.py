import abc
from typing import Optional

from universal_ci_noti.noti.types import JobResult


class NotificationQueue:
    def __init__(self):
        pass

    @abc.abstractmethod
    async def publish_job_result(self, job_result: JobResult):
        pass

    @abc.abstractmethod
    async def receive_job_result(self, timeout=None) -> Optional[JobResult]:
        pass
