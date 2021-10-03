from flask_app import app, db
from flask_app.models import User, Post


@app.shell_context_processor
def make_shell_context():  # For flask shell
    return {'db': db, 'User': User, 'Post': Post}


if __name__ == '__main__':
    app.run(debug=True)