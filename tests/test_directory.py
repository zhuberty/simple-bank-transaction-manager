from TransactionManager.Directory import Directory
from TransactionManager.utils import get_calling_file_dir


def test_directory_exist():
    assert Directory("test").exists() == False
    assert Directory(get_calling_file_dir(__file__)).exists() == True

def test_directory_str():
    assert str(Directory("test")) == "Directory: test"
    assert str(Directory(get_calling_file_dir(__file__))) == f"Directory: {get_calling_file_dir(__file__)}"
