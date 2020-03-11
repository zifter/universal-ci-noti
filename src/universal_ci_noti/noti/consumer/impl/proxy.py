import logging

from universal_ci_noti.noti.consumer import NotificationConsumer
from universal_ci_noti.noti.types import JobResult

logger = logging.getLogger("universal_ci_noti.noti.consumer.impl.proxy")


class ProxyConsumer(NotificationConsumer):
    def __init__(self, initial_consumer: NotificationConsumer):
        super().__init__()

        self._consumer: NotificationConsumer = initial_consumer

    async def on_job_finished(self, job_result: JobResult):
        await self._consumer.on_job_finished(job_result)
