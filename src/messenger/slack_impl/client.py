from slack import WebClient

from common.logger import g_logger
from messenger import Messanger
from messenger import MessageFormatter
from messenger.slack_impl.helper import SlackHelper
from messenger.slack_impl.formatter import SlackMessageFormatter


class SlackMessengerImpl(Messanger):
    def __init__(self, token):
        super().__init__()
        self._client = WebClient(token=token, run_async=True)
        self._helper = SlackHelper(self._client)
        self._formatter = SlackMessageFormatter(self._helper)

    def formatter(self) -> MessageFormatter:
        return self._formatter

    async def send_msg_to_user(self, user_id: str, msg: str):
        g_logger.info(f'Send by slack to {user_id} message {msg}')

        return await self._client.chat_postMessage(
            channel=await self._helper.get_slack_user_id(user_id),
            text=msg,
        )
