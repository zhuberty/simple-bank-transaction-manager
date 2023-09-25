import os

# get the calling file's directrory path
def get_calling_file_dir(file):
    """
    file: __file__ from the calling file.
    ex. get_calling_file_dir(__file__)
    """
    dir_path = os.path.dirname(os.path.realpath(file))
    file_path = os.path.join(dir_path, file)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    return dir_path
