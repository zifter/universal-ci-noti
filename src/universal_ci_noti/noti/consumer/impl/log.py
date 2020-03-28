import logging

from universal_ci_noti.noti.consumer import NotificationConsumer
from universal_ci_noti.noti.types import JobResult


class LogConsumer(NotificationConsumer):
    async def on_job_finished(self, job_result: JobResult):
        logging.info(f"Job finished: {job_result}")
