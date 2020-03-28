from universal_ci_noti.messenger import MessageFormatter

from .helper import SlackHelper


class SlackMessageFormatter(MessageFormatter):
    def __init__(self, helper: SlackHelper):
        self.helper = helper

    async def as_url(self, text, url):
        return f"<{url}|{text}>"

    async def user_id(self, user_id):
        user_id = await self.helper.get_slack_user_id(user_id)
        return f"<@{user_id}>"
