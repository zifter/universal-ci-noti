import asyncio
import logging
import os
import sys

from universal_ci_noti.messenger.slack_impl.client import SlackMessengerImpl
from universal_ci_noti.noti.consumer.impl.working_hours_filter import WorkingHoursFilter, WorkingHoursProviderDefault
from universal_ci_noti.noti.queue.impl import SimpleQueueImpl
from universal_ci_noti.noti.consumer.impl import FilterConsumer
from universal_ci_noti.noti.consumer.impl import PersonalMessageConsumer
from universal_ci_noti.noti.consumer.impl import ChannelMessageConsumer
from universal_ci_noti.noti.consumer.impl import LogConsumer
from universal_ci_noti.noti.consumer.impl import ContainerConsumer
from universal_ci_noti.noti.producer.impl import WebProducer
from universal_ci_noti.noti.runtime import NotificationRuntime, NotificationRuntimeExiter
from universal_ci_noti.web_server.impl import aiohttpWebAPI


SLACK_API_TOKEN = os.environ.get('SLACK_API_TOKEN')
SLACK_TEST_GROUP = os.environ.get('SLACK_TEST_GROUP')


def setup_logger():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    root.addHandler(handler)

async def main():
    setup_logger()

    messenger = SlackMessengerImpl(SLACK_API_TOKEN)
    web_api = aiohttpWebAPI()

    queue = SimpleQueueImpl()

    consumer = ContainerConsumer([
        LogConsumer(),
        FilterConsumer(
            [
                WorkingHoursFilter(WorkingHoursProviderDefault())
            ],
            ContainerConsumer([
                PersonalMessageConsumer(messenger),
                ChannelMessageConsumer(messenger, SLACK_TEST_GROUP),
            ]),
        )
    ])

    producers = [
        WebProducer(queue, web_api)
    ]

    runtime = NotificationRuntime(queue, consumer, producers)

    web_api.go()
    _ = NotificationRuntimeExiter(runtime)
    await runtime.go()


if __name__ == '__main__':
    asyncio.run(main())
