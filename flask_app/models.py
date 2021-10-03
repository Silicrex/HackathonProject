from flask_app import db, login
from datetime import datetime as Datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))  # str by default, convert to int


# Columns are fields
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # User account id
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    # backref for name for connected object. post.author will give user

    def __repr__(self):  # For printing/debugging
        return '<User {}>'.format(self.username)

    def set_password(self, password):  # Cryptographically hash password
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):  # Validate password
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=Datetime.utcnow)  # Function call given
    password_hash = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class PhysicalSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))  # Optional identification
    contact = db.Column(db.String(64))  # Optional contact
    body = db.Column(db.String(2000))
    timestamp = db.Column(db.DateTime, index=True, default=Datetime.utcnow)  # Function call given

    def __repr__(self):
        return (f'{self.id=}, {self.name=}, {self.contact=}, {self.body=}')


class MentalSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))  # Optional identification
    contact = db.Column(db.String(64))  # Optional contact
    body = db.Column(db.String(2000))
    timestamp = db.Column(db.DateTime, index=True, default=Datetime.utcnow)  # Function call given

    def __repr__(self):
        return (f'{self.id=}, {self.name=}, {self.contact=}, {self.body=}')


class HazardSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))  # Optional identification
    contact = db.Column(db.String(64))  # Optional contact
    body = db.Column(db.String(2000))
    timestamp = db.Column(db.DateTime, index=True, default=Datetime.utcnow)  # Function call given

    def __repr__(self):
        return (f'{self.id=}, {self.name=}, {self.contact=}, {self.body=}')


class DiversitySubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))  # Optional identification
    contact = db.Column(db.String(64))  # Optional contact
    body = db.Column(db.String(2000))
    timestamp = db.Column(db.DateTime, index=True, default=Datetime.utcnow)  # Function call given

    def __repr__(self):
        return (f'{self.id=}, {self.name=}, {self.contact=}, {self.body=}')


class ResourceSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))  # Optional identification
    contact = db.Column(db.String(64))  # Optional contact
    body = db.Column(db.String(2000))
    timestamp = db.Column(db.DateTime, index=True, default=Datetime.utcnow)  # Function call given

    def __repr__(self):
        return (f'{self.id=}, {self.name=}, {self.contact=}, {self.body=}')


class MiscSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))  # Optional identification
    contact = db.Column(db.String(64))  # Optional contact
    body = db.Column(db.String(2000))
    timestamp = db.Column(db.DateTime, index=True, default=Datetime.utcnow)  # Function call given

    def __repr__(self):
        return (f'{self.id=}, {self.name=}, {self.contact=}, {self.body=}')


class Resources(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(64))  # Optional identification
    desc = db.Column(db.String(128))  # Optional identification

    def __repr__(self):
        return (f'{self.id=}, {self.url=}, {self.desc=}')
