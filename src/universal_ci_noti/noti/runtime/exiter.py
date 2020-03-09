import signal

from universal_ci_noti.noti.runtime.runtime import NotificationRuntime


class NotificationRuntimeExiter:
    def __init__(self, runtime: NotificationRuntime):
        self._runtime = runtime

        self._override_signal()

    def _override_signal(self):
        signal.signal(signal.SIGINT, self.change_state)

    def _restore_signal(self):
        signal.signal(signal.SIGINT, signal.SIG_DFL)

    def change_state(self, signum, frame):
        logger.info(
            "Interrupt signal received, stopping runtime... repeat for force exit"
        )
        self._restore_signal()
        self._runtime.stop()
