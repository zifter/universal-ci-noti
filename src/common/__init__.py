from packaging import version
import platform

from common.fs import recreate_path, create_path
from common.project import tmp_dir, logs_dir
from common.process import is_main_process


if version.parse(platform.python_version()) < version.parse('3.7.1'):
    raise Exception(f"Must be using Python greater 3.7.1, current is {platform.python_version()}")


if is_main_process():
    recreate_path(tmp_dir())
    create_path(logs_dir())
