import asyncio
import threading
from typing import List, Optional

from common.logger import g_logger
from common.utils import ElapsedTime
from noti.queue import NotificationQueue
from noti.types import JobResult


class SimpleQueueImpl(NotificationQueue):
    def __init__(self):
        super().__init__()

        self._job_result: List[JobResult] = []
        self._lock = threading.Lock()

    async def publish_job_result(self, job_result: JobResult):
        g_logger.info(f'Publish job result {job_result} ')

        with self._lock:
            self._job_result.append(job_result)

    async def receive_job_result(self, timeout=None) -> Optional[JobResult]:
        timer = ElapsedTime()
        while timeout is None or timer.diff < timeout:
            if self._job_result:
                job = self._job_result.pop(0)

                g_logger.info(f'Receive job result {job}')

                return job

            await asyncio.sleep(1)

        return None
