from messenger import MessageFormatter
from messenger.slack_impl.helper import SlackHelper


class SlackMessageFormatter(MessageFormatter):
    def __init__(self, helper: SlackHelper):
        self.helper = helper

    async def as_url(self, text, url):
        return f'<{url}|{text}>'

    async def user_id(self, user_id):
        user_id = await self.helper.get_slack_user_id(user_id)
        return f'<@{user_id}>'
