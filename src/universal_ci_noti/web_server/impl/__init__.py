import asyncio
from threading import Thread
from typing import Optional

from aiohttp import web
from universal_ci_noti.utils import is_main_thread


class aiohttpWebAPI:
    def __init__(self, port: int = 8080):
        self._port = port
        self._app = web.Application()

        self.thread: Optional[Thread] = Thread(target=self._start_server_in_thread)

    def go(self):
        self.thread.start()

    def stop(self):
        self._app.shutdown()

        self.thread.join()

    def add_post_route(self, path: str, handler):
        async def wrapped_handler(request):
            await handler(await request.json())

            return web.Response()

        self._app.add_routes(
            [web.post(path, wrapped_handler),]
        )

    def _start_server_in_thread(self):
        assert is_main_thread() is False

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        web.run_app(self._app, port=self._port, handle_signals=False)
