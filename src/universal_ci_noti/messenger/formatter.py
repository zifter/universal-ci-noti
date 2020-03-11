class PlainFormatter:
    async def as_url(self, text, url):
        return f"{text}({url})"

    async def user_id(self, user_id):
        return f"[{user_id}]"
