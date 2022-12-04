"""Test the configuration  module."""
import os

def test_development_config(test_app):
    """Test development configuration."""
    test_app.config.from_object('src.config.DevelopmentConfig')
    assert not test_app.config['TESTING']
    assert test_app.config['UPLOAD_PATH'] == os.environ.get('UPLOAD_PATH')

def test_testing_config(test_app):
    """Test testing configuration."""
    test_app.config.from_object('src.config.TestingConfig')
    assert test_app.config['TESTING']
    assert test_app.config['UPLOAD_PATH_TEST'] == os.environ.get('UPLOAD_PATH_TEST')

def test_production_config(test_app):
    """Test production configuration."""
    test_app.config.from_object('src.config.ProductionConfig')
    assert not test_app.config['TESTING']
    assert test_app.config['UPLOAD_PATH'] == os.environ.get('UPLOAD_PATH')
