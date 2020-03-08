import abc
import asyncio
from typing import List, Optional

from common.utils import ElapsedTime
from noti.types import JobResult


class NotificationQueue:
    def __init__(self):
        pass

    @abc.abstractmethod
    async def publish_job_result(self, job_result: JobResult):
        pass

    @abc.abstractmethod
    async def receive_job_result(self, timeout=None) -> Optional[JobResult]:
        pass