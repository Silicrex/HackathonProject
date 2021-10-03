import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:  # 'or' used to provide default values if the environment variables are empty
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'base-password'  # For various tokens/signatures
    SQLALCHEMY_DATABASE_URI = (os.environ.get('DATABASE_URL') or  # Database location
                               'sqlite:///' + os.path.join(basedir, 'app.db'))  # Backup
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Signal to app for database changes
