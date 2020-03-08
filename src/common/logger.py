import logging
from logging import config
from common import project, fs
import sys
import os


DEFAULT_VERBOSE_FORMATTER = logging.Formatter("%(asctime)s.%(msecs)03d %(processName)s/%(module)s %(levelname)s: %(message)s", "%H:%M:%S")


def _get_logger_name(module_file_path):
    return os.path.splitext(os.path.basename(module_file_path))[0]


def _get_logger_path(module_file_path=None):
    if module_file_path is None:
        module_file_path = sys.argv[0]

    logger_logs_folder = project.logs_dir()
    if not project.path.isdir(logger_logs_folder):
        os.mkdir(logger_logs_folder)

    logger_path = project.path.join(logger_logs_folder, '{}.log'.format(_get_logger_name(module_file_path)))

    return project.path.abspath(logger_path)


def get_log_level():
    default_level = logging.getLevelName(logging.DEBUG)
    level = os.getenv('PYTHON_LOG_LEVEL', default_level)
    return level


def setup_logger():
    module_path = sys.argv[0]
    log_filename = _get_logger_path(module_path)

    ini_file = project.settings_ini()
    if fs.exists(ini_file):
        config.fileConfig(ini_file, disable_existing_loggers=False, defaults={
            'log_filename': log_filename.replace('\\', '/'),
            'max_file_size': 1024*1024*20,  # 20mb
            'log_level': get_log_level(),
        })
    else:
        print(f'File does not exist {ini_file}')

    logger = logging.getLogger()

    return logger


g_logger = setup_logger()
