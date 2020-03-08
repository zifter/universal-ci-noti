import asyncio
import os

from common.arg_parser import ArgParser
from noti.queue.impl import SimpleQueueImpl
from noti.consumer.impl import MessengerConsumer
from noti.producer.impl import WebProducer
from messenger.slack_impl.client import SlackMessengerImpl
from noti.runtime import NotificationRuntime, NotificationRuntimeExiter


def get_context():
    parser = ArgParser()
    parser.add_argument('--slack-api-token', default=os.environ.get('SLACK_API_TOKEN'))
    return parser.parse_args()


async def main(context):
    messenger = SlackMessengerImpl(context.slack_api_token)

    queue = SimpleQueueImpl()
    consumer = MessengerConsumer(messenger)
    producer = WebProducer(queue)
    runtime = NotificationRuntime(queue, [consumer], [producer])

    _ = NotificationRuntimeExiter(runtime)
    await runtime.go()


if __name__ == '__main__':
    asyncio.run(main(get_context()))
