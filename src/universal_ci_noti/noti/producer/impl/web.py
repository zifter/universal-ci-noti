import asyncio
import json
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
from typing import Optional

from universal_ci_noti.noti.producer import NotificationProducer
from universal_ci_noti.noti.queue import NotificationQueue
from universal_ci_noti.noti.types import JobResult

logger = logging.getLogger("universal_ci_noti.messenger.slack_impl")


# HTTP server is piece of shit
# rewrite it

_QUEUE: NotificationQueue = None
_SERVER: HTTPServer = None


class SimpleNotificationHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("Waiting for post messages")

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)

        if self.path == "/job-result/":
            data = json.loads(body)
            result = JobResult.from_json(data)

            logger.info(f"Receive job result {result} by web")

            global _QUEUE
            asyncio.run(_QUEUE.publish_job_result(result))
            self.send_response(200)
            self.end_headers()
        elif self.path == "/jenkins/job-finalized/":
            # TODO
            self.send_error(404, f"Jenkins is not supported")
        else:
            self.send_error(404, f"Undefined notification type: {self.path}")


def _start_server():
    _SERVER.serve_forever()


class WebProducer(NotificationProducer):
    def __init__(self, queue, port=8080):
        super().__init__(queue)

        global _QUEUE
        _QUEUE = queue

        global _SERVER
        _SERVER = HTTPServer(("", port), SimpleNotificationHandler)

        self.thread: Optional[Thread] = Thread(target=_start_server)

    async def go(self):
        self.thread.start()

    async def exit(self):
        logger.info("Stop http server")
        global _SERVER
        _SERVER.server_close()

        logger.info("join thread")
        try:
            self.thread.join()
        except:
            pass
