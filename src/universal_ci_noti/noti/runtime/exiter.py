import logging
import signal

from universal_ci_noti.noti.runtime.runtime import NotificationRuntime

logger = logging.getLogger("universal_ci_noti.noti.runtime")


class NotificationRuntimeExiter:
    def __init__(self, runtime: NotificationRuntime):
        self._runtime = runtime

        self._override_signal()

    def _override_signal(self):
        signal.signal(signal.SIGINT, self._change_state)

    def _restore_signal(self):
        signal.signal(signal.SIGINT, signal.SIG_DFL)

    def _change_state(self, *_):
        logger.info(
            "Interrupt signal received, stopping runtime... repeat for force exit"
        )
        self._restore_signal()
        self._runtime.stop()
