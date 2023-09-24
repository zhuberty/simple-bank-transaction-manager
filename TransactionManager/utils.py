import os

# get the calling file's directrory path
def get_calling_file_dir():
    return os.path.dirname(os.path.realpath(__file__))
