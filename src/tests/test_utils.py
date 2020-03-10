from universal_ci_noti.utils import is_main_process, is_main_thread


def test_main_thread():
    assert is_main_process() is True
    assert is_main_thread() is True
