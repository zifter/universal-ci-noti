import sys
from os import path, getcwd
from os.path import pardir


def working_dir():
    return getcwd()


def project_dir():
    if path.splitext(sys.argv[0])[1] == '.exe':
        return getcwd()
    else:
        return path.abspath(path.join(__file__, pardir, pardir, pardir))


def venv_dir():
    return path.join(project_dir(), 'venv')


def tmp_dir():
    return path.join(project_dir(), '_tmp')


def logs_dir():
    return path.join(project_dir(), '_logs')


def settings_ini():
    return path.join(project_dir(), 'settings.ini')
