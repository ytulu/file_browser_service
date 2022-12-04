"""
The test config is used to override the default config for testing.
"""
import os
import pytest

from src import app

UPLOAD_PATH_TEST = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_files',
    )

FIXTURE_NONEMPTY_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_files', 'nonempty_dir')

FIXTURE_HIDDEN_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'test_files', '.hidden_dir')

@pytest.fixture(scope='module')
def test_app():
    """Create and configure a new app instance for each test."""
    app.config.from_object('src.config.TestingConfig')
    # Create the app with common test config
    with app.app_context():
        yield app

@pytest.fixture
def empty_dir():
    '''Returns an empty directory'''
    return os.path.join(FIXTURE_DIR, 'empty_dir')

@pytest.fixture
def empty_dir_contents():
    '''Returns the contents of an empty directory'''
    return []

@pytest.fixture
def nonempty_dir():
    '''Returns a non-empty directory'''
    return FIXTURE_NONEMPTY_DIR

def nonempty_dir_contents():
    '''Returns the contents of a non-empty directory'''
    return [
        os.path.join(FIXTURE_NONEMPTY_DIR, 'dir.json'),
        os.path.join(FIXTURE_NONEMPTY_DIR, 'file.txt'),
        os.path.join(FIXTURE_NONEMPTY_DIR, 'not_allowed.jpg'),
        ]

@pytest.fixture
def hidden_dir():
    '''Returns a hidden directory'''
    return os.path.join(FIXTURE_DIR, '.hidden_dir')

@pytest.fixture
def hidden_dir_contents():
    '''Returns the contents of a hidden directory'''
    return os.path.join(FIXTURE_HIDDEN_DIR, '.hiden.txt')

@pytest.fixture
def empty_file():
    '''Returns an empty file'''
    return os.path.join(FIXTURE_DIR, 'empty.txt')

@pytest.fixture
def empty_file_contents():
    '''Returns the contents of an empty file'''
    return ''

@pytest.fixture
def empty_file_json():
    '''Returns the contents of an empty json file'''
    return os.path.join(FIXTURE_DIR, 'empty.json')

@pytest.fixture
def empty_file_json_contents():
    '''Returns the contents of an empty json file'''
    return ''

@pytest.fixture
def non_empty_file():
    '''Returns a non-empty file'''
    return os.path.join(FIXTURE_NONEMPTY_DIR, 'non_empty.txt')

@pytest.fixture
def non_empty_file_contents():
    '''Returns the contents of a non-empty file'''
    return 'the quick brown fox jumps over the lazy dog'

@pytest.fixture
def non_empty_file_json():
    '''Returns a non-empty json file'''
    return os.path.join(FIXTURE_NONEMPTY_DIR, 'non_empty.json')

@pytest.fixture
def not_allowed_file():
    ''' Returns a file with an extension not allowed'''
    return os.path.join(FIXTURE_DIR, 'not_allowed.jpg')

@pytest.fixture
def not_allowed_file_contents():
    '''Returns the contents of a file with an extension not allowed'''
    return ''

@pytest.fixture
def hidden_file():
    '''Returns a hidden file'''
    return os.path.join(FIXTURE_DIR, '.hidden.txt')

@pytest.fixture
def hidden_file_contents():
    '''Returns the contents of a hidden file'''
    return 'hiden file'