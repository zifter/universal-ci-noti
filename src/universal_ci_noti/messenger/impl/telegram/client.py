import logging

from aioify import aioify
from telegram import Bot

from universal_ci_noti.messenger import MessageFormatter, Messanger

from .formatter import TelegramMessageFormatter


class TelegramMessenger(Messanger):
    def __init__(self, token):
        super().__init__()
        self._bot: Bot = Bot(token=token)
        self._formatter: TelegramMessageFormatter = TelegramMessageFormatter()

        logging.info(self._bot.get_me())

    def formatter(self) -> MessageFormatter:
        return self._formatter

    async def send_msg_to_user(self, user_id: str, msg: str):
        logging.info(f"Send by telegram to {user_id} message {msg}")

        # raise NotImplementedError("It's much complicated to send message to user")
        # return await aioify(self._bot.send_message)(chat_id=user_id, text=msg, parse_mode=self._formatter.parse_mode)

    async def send_msg_to_channel(self, channel_id: str, msg: str):
        logging.info(f"Send by slack to {channel_id} message {msg}")

        return await aioify(self._bot.send_message)(
            chat_id=int(channel_id), text=msg, parse_mode=self._formatter.parse_mode
        )
