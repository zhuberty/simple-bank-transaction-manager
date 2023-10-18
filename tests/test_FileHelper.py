import os
import pytest
from TransactionManager.FileHelper import FileHelper

def test_get_cwd():
    assert FileHelper.get_cwd(__file__).endswith("tests")

def test_get_dirpath():
    assert FileHelper.get_dirpath(__file__, "test_data").endswith("test_data")

def test_path_exists():
    assert FileHelper.path_exists(FileHelper.get_cwd(__file__))
    assert not FileHelper.path_exists("this/path/does/not/exist")

def test_list_dirs():
    test_data_dir = os.path.join(FileHelper.get_dirpath(__file__, "./test_data"))
    assert FileHelper.list_dirs(test_data_dir) == ["accounts"]
    with pytest.raises(FileNotFoundError):
        assert FileHelper.list_dirs("this/path/does/not/exist") == []