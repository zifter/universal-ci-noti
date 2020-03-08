import signal
from typing import List

from common.logger import g_logger
from noti.consumer import NotificationConsumer
from noti.producer import NotificationProducer
from noti.queue import NotificationQueue


class NotificationRuntime:
    def __init__(self, queue: NotificationQueue, consumers: List[NotificationConsumer], producers: List[NotificationProducer]):
        self._queue = queue
        self._consumers = consumers
        self._producers = producers

        self.is_running = False

    async def go(self):
        for producer in self._producers:
            g_logger.info(f'Go producer... {producer}')
            await producer.go()

        g_logger.info(f'Start event loop')
        self.is_running = True
        while self.is_running:
            job_result = await self._queue.receive_job_result(timeout=1)
            if job_result:
                for consumer in self._consumers:
                    g_logger.debug(f'sent to consumer... {consumer}')
                    g_logger.debug(job_result)
                    await consumer.on_job_finished(job_result)

        g_logger.info(f'Event loop finished')

        for producer in self._producers:
            g_logger.info(f'Exit producer... {producer}')
            await producer.exit()

        g_logger.info(f'Runtime has finished. Goodbye!')

    def stop(self):
        g_logger.info(f'Stop runtime...')
        self.is_running = False


class NotificationRuntimeExiter:
    def __init__(self, runtime: NotificationRuntime):
        self._runtime = runtime

        self._override_signal()

    def _override_signal(self):
        signal.signal(signal.SIGINT, self.change_state)

    def _restore_signal(self):
        signal.signal(signal.SIGINT, signal.SIG_DFL)

    def change_state(self, signum, frame):
        g_logger.info('Interrupt signal received, stopping runtime... repeat for force exit')
        self._restore_signal()
        self._runtime.stop()
