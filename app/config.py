# app/config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-default-unsafe-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///default_dev.db' # Default for local dev
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config): # Inherits from Config, but overrides specifics
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' # Use in-memory DB for tests
    WTF_CSRF_ENABLED = False # Disable CSRF for easier form testing
    SERVER_NAME = "localhost.localdomain" # Helps with url_for in tests