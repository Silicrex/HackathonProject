from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)  # The central Flask instance
app.config.from_object(Config)  # Load config from Config class
db = SQLAlchemy(app)  # Database instance
migrate = Migrate(app, db)  # Migration engine instance

from flask_app import routes, models  # Import below to avoid circular import
