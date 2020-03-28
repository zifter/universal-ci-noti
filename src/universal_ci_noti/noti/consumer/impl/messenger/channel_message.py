import logging

from universal_ci_noti.messenger import Messanger
from universal_ci_noti.noti.consumer import NotificationConsumer
from universal_ci_noti.noti.types import JobResult


class ChannelMessageConsumer(NotificationConsumer):
    def __init__(self, messenger, channel_id: str):
        super().__init__()

        self.messenger: Messanger = messenger
        self.channel_id: str = channel_id

    async def on_job_finished(self, job_result: JobResult):
        logging.info(f"Create message for chat")

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

        await self.messenger.send_msg_to_channel(self.channel_id, msg)
