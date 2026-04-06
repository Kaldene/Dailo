from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(70), index=True, unique=True, nullable=False)
    email = db.Column(db.String(200), index=True, unique=True, nullable=False)
    hashed_password = db.Column(db.String(300))

    task =db.relationship('Task', backref='user', lazy='select', cascade='all, delete-orphan')

    def __repr__(self):
        return '<User %r>' % self.username