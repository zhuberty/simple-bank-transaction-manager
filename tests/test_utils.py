import pytest

from TransactionManager.utils import get_cwd, get_filepath, path_exists

def test_get_cwd():
    assert get_cwd(__file__).endswith("tests")

def test_get_filepath():
    assert get_filepath(__file__, "test_data").endswith("tests/test_data")

def test_path_exists():
    assert path_exists(get_cwd(__file__))
    assert not path_exists("this/path/does/not/exist")