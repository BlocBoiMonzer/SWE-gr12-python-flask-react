from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from configparser import ConfigParser

def migrate():
    return None