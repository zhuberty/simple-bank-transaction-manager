import os
import pytest

from TransactionManager.utils import get_cwd, get_dirpath, path_exists, list_dirs

def test_get_cwd():
    assert get_cwd(__file__).endswith("tests")

def test_get_dirpath():
    assert get_dirpath(__file__, "test_data").endswith("tests/test_data")

def test_path_exists():
    assert path_exists(get_cwd(__file__))
    assert not path_exists("this/path/does/not/exist")

def test_list_dirs():
    test_data_dir = os.path.join(get_dirpath(__file__, "./test_data"))
    assert list_dirs(test_data_dir) == ["accounts"]
    with pytest.raises(FileNotFoundError):
        assert list_dirs("this/path/does/not/exist") == []