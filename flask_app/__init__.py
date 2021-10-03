from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = Flask(__name__)  # The central Flask instance
app.config.from_object(Config)  # Load config from Config class
db = SQLAlchemy(app)  # Database instance
migrate = Migrate(app, db)  # Migration engine instance
login = LoginManager(app)  # Login handler instance
login.login_view = 'login'  # Inform Flask-Login of the login view function
boostrap = Bootstrap(app)

from flask_app import routes, models  # Import below to avoid circular import
