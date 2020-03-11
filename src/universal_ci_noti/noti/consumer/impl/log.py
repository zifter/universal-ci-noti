import logging

from universal_ci_noti.noti.consumer import NotificationConsumer
from universal_ci_noti.noti.types import JobResult

logger = logging.getLogger("universal_ci_noti.noti.consumer.impl.log")


class LogConsumer(NotificationConsumer):
    async def on_job_finished(self, job_result: JobResult):
        logger.info(f"Job finished: {job_result}")
