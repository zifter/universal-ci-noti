import asyncio
from typing import List

from universal_ci_noti.noti.consumer import NotificationConsumer
from universal_ci_noti.noti.types import JobResult


class ContainerConsumer(NotificationConsumer):
    def __init__(self, consumers: List[NotificationConsumer]):
        super().__init__()

        self._consumers: List[NotificationConsumer] = consumers

    async def on_job_finished(self, job_result: JobResult):
        tasks = [consumer.on_job_finished(job_result) for consumer in self._consumers]
        await asyncio.gather(*tasks)
