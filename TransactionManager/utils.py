import os

def get_cwd(file):
    """
    file: __file__ from the calling file.
    ex. get_cwd(__file__)
    """
    return os.path.dirname(os.path.realpath(file))

def get_filepath(file, dir):
    """
    file: __file__ from the calling file.
    dir: the directory to get the file from.
    ex. get_filepath(__file__, "test_data")
    """
    return os.path.join(get_cwd(file), dir)

def path_exists(path):
    return os.path.exists(path)