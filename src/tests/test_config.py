"""Test the configuration  module."""
import os


def test_development_config(test_app):
    """Test development configuration."""
    test_app.config.from_object("src.config.DevelopmentConfig")
    assert not test_app.config["TESTING"]
    upload_path = os.environ.get("UPLOAD_PATH")
    assert test_app.config["UPLOAD_PATH"] == upload_path


def test_testing_config(test_app):
    """Test testing configuration."""
    test_app.config.from_object("src.config.TestingConfig")
    assert test_app.config["TESTING"]
    test_path = os.environ.get("UPLOAD_PATH_TEST")
    assert test_app.config["UPLOAD_PATH_TEST"] == test_path


def test_production_config(test_app):
    """Test production configuration."""
    test_app.config.from_object("src.config.ProductionConfig")
    assert not test_app.config["TESTING"]
    assert test_app.config["UPLOAD_PATH"] == os.environ.get("UPLOAD_PATH")
