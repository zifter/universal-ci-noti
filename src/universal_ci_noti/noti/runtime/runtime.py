import logging
from typing import List

from universal_ci_noti.noti.consumer import NotificationConsumer
from universal_ci_noti.noti.producer import NotificationProducer
from universal_ci_noti.noti.queue import NotificationQueue

logger = logging.getLogger("universal_ci_noti.noti.runtime")


class NotificationRuntime:
    def __init__(
        self,
        queue: NotificationQueue,
        consumers: List[NotificationConsumer],
        producers: List[NotificationProducer],
    ):
        self._queue = queue
        self._consumers = consumers
        self._producers = producers

        self.is_running = False

    async def go(self):
        for producer in self._producers:
            logger.info(f"Go producer... {producer}")
            await producer.go()

        logger.info(f"Start event loop")
        self.is_running = True
        while self.is_running:
            job_result = await self._queue.receive_job_result(timeout=1)
            if job_result:
                for consumer in self._consumers:
                    logger.debug(f"sent to consumer... {consumer}")
                    logger.debug(job_result)
                    await consumer.on_job_finished(job_result)

        logger.info(f"Event loop finished")

        for producer in self._producers:
            logger.info(f"Exit producer... {producer}")
            await producer.exit()

        logger.info(f"Runtime has finished. Goodbye!")

    def stop(self):
        logger.info(f"Stop runtime...")
        self.is_running = False
