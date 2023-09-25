import pytest

from TransactionManager.utils import get_calling_file_dir

def test_get_calling_file_dir():
    assert get_calling_file_dir(__file__).endswith("tests")
    # assert that it throws an error if the file doesn't exist
    with pytest.raises(FileNotFoundError):
        get_calling_file_dir("not_a_file.txt")
