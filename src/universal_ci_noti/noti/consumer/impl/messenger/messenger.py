import logging

from universal_ci_noti.messenger import Messanger
from universal_ci_noti.noti.consumer import NotificationConsumer
from universal_ci_noti.noti.types import JobResult

logger = logging.getLogger("universal_ci_noti.noti.consumer.impl.messenger")


class MessengerConsumer(NotificationConsumer):
    def __init__(self, messenger):
        super().__init__()

        self.messenger: Messanger = messenger

    async def on_job_finished(self, job_result: JobResult):
        logger.info(f"Create message for chat")

        formatter = self.messenger.formatter()

        repo_text = await formatter.as_url(
            job_result.build.scm.name, job_result.build.scm.url
        )
        job_page = await formatter.as_url("Build page", job_result.url)
        user_mention = await formatter.user_id(job_result.build.scm.committer)

        msg = (
            f"🖥 Building {repo_text}: {job_result.build.status}\n"
            f"Branch: {job_result.build.scm.branch}\n"  # TODO Branch url also
            f"Committer: {user_mention}\n"
            f"{job_page}"
        )

        await self.messenger.send_msg_to_user(job_result.build.scm.committer, msg)
