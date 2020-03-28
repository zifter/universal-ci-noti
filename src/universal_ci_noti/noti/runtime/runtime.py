import logging
from typing import List

from universal_ci_noti.noti.consumer import NotificationConsumer
from universal_ci_noti.noti.producer import NotificationProducer
from universal_ci_noti.noti.queue import NotificationQueue


class NotificationRuntime:
    def __init__(
        self,
        queue: NotificationQueue,
        consumer: NotificationConsumer,
        producers: List[NotificationProducer],
    ):
        self._queue = queue
        self._consumer = consumer
        self._producers = producers

        self.is_running = False

    async def go(self):
        for producer in self._producers:
            logging.info(f"Go producer... {producer}")
            await producer.go()

        logging.info(f"Start event loop")
        self.is_running = True
        while self.is_running:
            job_result = await self._queue.receive_job_result(timeout=1)
            if job_result:
                logging.debug(f"sent job result... {job_result}")
                await self._consumer.on_job_finished(job_result)

        logging.info(f"Event loop finished")

        for producer in self._producers:
            logging.info(f"Exit producer... {producer}")
            await producer.exit()

        logging.info(f"Runtime has finished. Goodbye!")

    def stop(self):
        logging.info(f"Stop runtime...")
        self.is_running = False
