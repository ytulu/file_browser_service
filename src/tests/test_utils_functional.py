import os
from pathlib import Path

import pytest

from src.utils import get_file_attr


@pytest.fixture
def base_path() -> Path:
    """Get the current folder of the test"""
    return Path(__file__).parent


def test__get_file_attr(base_path: Path):
    """
    GIVEN a fileModel class
    WHEN a new fileModel is created
    THEN check the fileModel name, path, size,
         and permissions are defined correctly
    """
    test_files = os.path.join(base_path, "test_files")
    file = os.path.join(test_files, "test.txt")
    file_atr_obj = get_file_attr(file)
    assert file_atr_obj["name"] == os.path.basename(file)
    assert file_atr_obj["owner"] == os.stat(file).st_uid
    assert file_atr_obj["size"] == os.stat(file).st_size
    assert file_atr_obj["permissions"] == os.stat(file).st_mode
