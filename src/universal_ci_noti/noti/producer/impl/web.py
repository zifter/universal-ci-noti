import logging

from universal_ci_noti.noti.producer import NotificationProducer
from universal_ci_noti.noti.queue import NotificationQueue
from universal_ci_noti.noti.types import JobResult
from universal_ci_noti.web_server import WebAPI

logger = logging.getLogger("universal_ci_noti.messenger.slack_impl")


class WebProducer(NotificationProducer):
    def __init__(self, queue: NotificationQueue, webAPI: WebAPI):
        super().__init__(queue)

        webAPI.add_post_route("/job-result/", self._on_job_result)

    async def go(self):
        logger.info("Start Web API producer")

    async def exit(self):
        logger.info("Stop Web API producer")

    async def _on_job_result(self, data):
        result = JobResult.from_dict(data)
        logger.info(f"Receive job result {result} by web")
        await self.queue.publish_job_result(result)
