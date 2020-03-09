import abc


class MessageFormatter:
    @abc.abstractmethod
    async def as_url(self, text, url):
        pass

    @abc.abstractmethod
    async def user_id(self, user_id):
        pass


class Messanger:
    def __init__(self):
        pass

    @abc.abstractmethod
    def formatter(self) -> MessageFormatter:
        pass

    @abc.abstractmethod
    async def send_msg_to_user(self, user_id: str, msg: str):
        """
        Send message to user

        :param user_id:
        :param msg:
        :return:
        """
