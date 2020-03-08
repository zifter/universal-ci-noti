from os import path, makedirs, listdir, remove, walk, stat
import shutil
import fnmatch
from time import sleep


def recreate_path(p, repeats=2):
    while repeats > 0:
        repeats = repeats - 1

        try:
            if path.exists(p):
                shutil.rmtree(p)

            makedirs(p)

            break
        except:

            if repeats == 0:
                raise
            else:
                sleep(1)

    return p


def create_path(p):
    if not path.exists(p):
        makedirs(p)

    return p


def copy_tree(src, dest, ignore_ext: set = None, ignore=None, symlinks=False):
    def ignore_ext_callback(src, names):
        a = [x for x in names if path.splitext(x)[1] in ignore_ext]
        return a

    if ignore_ext:
        ignore = ignore_ext_callback

    return shutil.copytree(src, dest, ignore=ignore, symlinks=symlinks)


def copy(src, dest):
    return shutil.copy(src, dest)


def rmtree(src):
    return shutil.rmtree(src)


def exists(p):
    return path.exists(p)


def remove_object(item):
    if exists(item):
        if path.isfile(item):
            remove(item)
        elif path.isdir(item):
            rmtree(item)
        else:
            assert False


def remove_files_by_pattern(folder, pattern):
    for root, dirs, files in walk(folder):
        for obj in fnmatch.filter(files + dirs, pattern):
            remove_object(path.join(root, obj))


def make_abspath(p):
    if path.isabs(p):
        return p
    else:
        return path.abspath(p)


def move_file(src, dest):
    shutil.move(src, dest)


def is_dir(src):
    return path.isdir(src)


__all__ = [
    'path',
    'walk',
    'stat',
    'listdir',
    'recreate_path',
    'create_path',
    'copy_tree',
    'copy',
    'rmtree',
    'exists',
    'remove_object',
    'remove_files_by_pattern',
    'make_abspath',
    'move_file',
    'is_dir',
]
