"""
This contains unit tests for the models.py file.
"""
from src.models import fileModel
from src.utils import allowed_file


def test_file_model_init():
    """
    GIVEN a fileModel class
    WHEN a new fileModel is created
    THEN check the fileModel name, path, size,
        and permissions are defined correctly
    """
    filename = "test.txt"
    owner = "test"
    size = 0
    permissions = 0o644
    file = fileModel(filename, owner, size, permissions)
    assert file.filename == filename
    assert file.owner == owner
    assert file.size == size
    assert file.permissions == permissions


def test_file_model_allowed_txt_file():
    """
    GIVEN a fileModel class
    WHEN a new fileModel is created
    THEN check the fileModel name, path, size,
         and permissions are defined correctly
    """
    filename = "test.txt"
    owner = "test"
    size = 0
    permissions = 0o644
    file = fileModel(filename, owner, size, permissions)
    assert allowed_file(file.filename) is True


def test_file_model_allowed_json_file():
    """
    GIVEN a fileModel class
    WHEN a new fileModel is created
    THEN check the fileModel name, path, size,
        and permissions are defined correctly
    """
    filename = "test.json"
    owner = "test"
    size = 0
    permissions = 0o644
    file = fileModel(filename, owner, size, permissions)
    assert allowed_file(file.filename) is True


def test_file_model_not_allowed_file():
    """
    GIVEN a fileModel class
    WHEN a new fileModel is created
    THEN check the fileModel name, path, size,
         and permissions are defined correctly
    """
    filename = "test.jpg"
    owner = "test"
    size = 0
    permissions = 0o644
    file = fileModel(filename, owner, size, permissions)
    assert allowed_file(file.filename) is False
