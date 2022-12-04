import os

class BaseConfig:
    """Base configuration"""
    TESTING = False
    UPLOAD_PATH = os.environ.get('UPLOAD_PATH')


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    UPLOAD_PATH = os.environ.get('UPLOAD_PATH')


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    UPLOAD_PATH = os.path.join(os.path.dirname(\
        os.path.dirname(os.path.abspath(__file__))), 'tests', 'test_files')


class ProductionConfig(BaseConfig):
    """Production configuration"""
    UPLOAD_PATH = os.environ.get('UPLOAD_PATH')
