import abc

from noti.types import JobResult


class NotificationConsumer:
    def __init__(self):
        pass

    @abc.abstractmethod
    async def on_job_finished(self, job_result: JobResult):
        """

        :rtype: object
        """
