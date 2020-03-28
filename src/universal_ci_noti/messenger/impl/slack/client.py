import logging

from slack import WebClient

from universal_ci_noti.messenger import MessageFormatter, Messanger

from .formatter import SlackMessageFormatter
from .helper import SlackHelper


class SlackMessenger(Messanger):
    def __init__(self, token):
        super().__init__()
        self._client = WebClient(token=token, run_async=True)
        self._helper = SlackHelper(self._client)
        self._formatter = SlackMessageFormatter(self._helper)

    def formatter(self) -> MessageFormatter:
        return self._formatter

    async def send_msg_to_user(self, user_id: str, msg: str):
        logging.info(f"Send by slack to {user_id} message {msg}")

        return await self._client.chat_postMessage(
            channel=await self._helper.get_slack_user_id(user_id), text=msg,
        )

    async def send_msg_to_channel(self, channel_id: str, msg: str):
        logging.info(f"Send by slack to {channel_id} message {msg}")

        return await self._client.chat_postMessage(channel=channel_id, text=msg)
