import os

def get_cwd(file) -> str:
    """
    file: __file__ from the calling file.
    ex. get_cwd(__file__)
    """
    return os.path.dirname(os.path.realpath(file))

def get_dirpath(file, dir) -> str:
    """
    file: __file__ from the calling file.
    dir: the directory to get the path for.
    ex. get_dirpath(__file__, "test_data")
    """
    return os.path.join(get_cwd(file), dir)

def path_exists(path):
    return os.path.exists(path)

def list_dirs(path) -> list:
    dirs = []
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            if item.startswith("__"):
                continue
            else:
                dirs.append(item)
    return dirs