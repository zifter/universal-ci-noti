from common.logger import g_logger
from messenger import Messanger
from noti.consumer import NotificationConsumer
from noti.types import JobResult


class MessengerConsumer(NotificationConsumer):
    def __init__(self, messenger):
        super().__init__()

        self.messenger: Messanger = messenger

    async def on_job_finished(self, job_result: JobResult):
        g_logger.info(f'Create message for chat')

        formatter = self.messenger.formatter()

        repo_text = await formatter.as_url(job_result.scm.repo_name, job_result.scm.repo_url)
        job_page = await formatter.as_url('Build page', job_result.job_url)
        user_mention = await formatter.user_id(job_result.scm.last_committer)

        msg = (f"🖥 Building {repo_text}: {job_result.status}\n"
               f"Branch: {job_result.scm.branch}\n"  # TODO Branch url also
               f"Committer: {user_mention}\n"
               f"{job_page}"
               )

        await self.messenger.send_msg_to_user(job_result.scm.last_committer, msg)
