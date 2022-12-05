import os


class BaseConfig:
    """Base configuration"""

    TESTING = False
    UPLOAD_PATH = os.environ.get("UPLOAD_PATH")


class DevelopmentConfig(BaseConfig):
    """Development configuration"""

    UPLOAD_PATH = os.environ.get("UPLOAD_PATH")


class TestingConfig(BaseConfig):
    """Testing configuration"""

    TESTING = True
    UPLOAD_PATH_TEST = os.environ.get("UPLOAD_PATH_TEST")


class ProductionConfig(BaseConfig):
    """Production configuration"""

    UPLOAD_PATH = os.environ.get("UPLOAD_PATH")
