from app import db
from sqlalchemy.dialects.postgresql import JSON

class User(db.model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable = False, unique=True)
    password = db.Column(db.String(), nullable = False)
    # backrefs
    polls = db.relationship('Poll', backref='user', order_by="Poll.created_at")
    votes  =db.relationship('Vote', backref='user')

    # def __init__(self, username, password):


class Poll(db.Model):
    __tablename__ = 'polls'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable = False)
    description = db.Column(db.String())
    created_at = db.Column(db.DateTime, nullable = False)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    options = db.relationship('Option', backref='poll', order_by="Option.created_at")

class Option(db.Model):
    __tablename__ = 'options'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime, nullable = False)
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'), nullable=False)

    votes = db.relationship('Vote', backref='option')
class Vote(db.Model):
    __tablename__ = 'votes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    option_id = db.Column(db.Integer, db.ForeignKey('option.id'), nullable=False)
