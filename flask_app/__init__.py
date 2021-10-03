from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from flask_app import routes  # Import below to avoid circular import