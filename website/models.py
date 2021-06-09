# create the database models
# import from current package which is 'notesDatabase.db'
# from website import db
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


#  define the class, to make a new database model, define name of the object then inherit from db.model
# foreign key is a key on column that references a collumn of another database
# for every note we want to store the id of user that created it
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # define the schema (columns/layout) of models. What do we want to store?
    # 150 is max length, unique=true makes is unable to be duplicated for another user


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    notes = db.relationship('Note')

# to add homepage photos
# class home_jpg(db.Model):
# id = db.Column(db.Integer, primary_key=True)
