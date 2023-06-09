import os


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = True if os.getenv('DEBUG_MODE', 'False') == 'True' else False
    SQLALCHEMY_ECHO = True if os.getenv('DEBUG_MODE', 'False') == 'True' else False
    JSON_AS_ASCII = False
    ORIGINAL_LINK_LENGTH = 512
    SHORT_ID_LENGTH = 16
