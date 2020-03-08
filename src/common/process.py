from multiprocessing import current_process


def is_main_process() -> bool:
    return current_process().name == 'MainProcess'
