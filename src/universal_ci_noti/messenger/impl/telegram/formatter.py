from universal_ci_noti.messenger import MessageFormatter


class TelegramMessageFormatter(MessageFormatter):
    def __init__(self,):
        self.parse_mode = "markdown"

    async def as_url(self, text, url):
        return f"[{text}]({url})"

    async def user_id(self, user_id):
        return f"@{user_id}"
