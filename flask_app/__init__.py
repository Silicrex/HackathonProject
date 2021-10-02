from flask import Flask

app = Flask(__name__)  # Flask app object

from flask_app import routes  # Below app definition to avoid circular import. Routes needs app
