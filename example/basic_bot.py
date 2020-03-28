import asyncio
import os

from universal_ci_noti.messenger.slack_impl.client import SlackMessengerImpl
from universal_ci_noti.noti.consumer.impl.filter import FilterConsumer
from universal_ci_noti.noti.consumer.impl.working_hours_filter import WorkingHoursFilter, WorkingHoursProviderDefault
from universal_ci_noti.noti.queue.impl import SimpleQueueImpl
from universal_ci_noti.noti.consumer.impl import MessengerConsumer, LogConsumer
from universal_ci_noti.noti.producer.impl import WebProducer
from universal_ci_noti.noti.runtime import NotificationRuntime, NotificationRuntimeExiter
from universal_ci_noti.web_server.impl import aiohttpWebAPI


async def main(context):
    messenger = SlackMessengerImpl(os.environ.get('SLACK_API_TOKEN'))
    web_api = aiohttpWebAPI()

    queue = SimpleQueueImpl()

    messenger_consumer = MessengerConsumer(messenger)
    filtered = FilterConsumer(messenger_consumer, [WorkingHoursFilter(WorkingHoursProviderDefault())])

    producer = WebProducer(queue, web_api)
    runtime = NotificationRuntime(queue, [filtered, LogConsumer()], [producer])

    web_api.go()
    _ = NotificationRuntimeExiter(runtime)
    await runtime.go()


if __name__ == '__main__':
    asyncio.run(main(get_context()))
