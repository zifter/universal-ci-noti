import abc


class WebAPI:
    @abc.abstractmethod
    def go(self):
        """
        Start web api
        """

    @abc.abstractmethod
    def stop(self):
        """
        Stop web api
        """

    @abc.abstractmethod
    def add_post_route(self, path: str, handler):
        """
        Add route to web api
        :param path:
        :param handler:
        :return:
        """
