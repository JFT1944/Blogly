"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
db = SQLAlchemy()

def connect_db(app):

    db.app = app
    db.init_app(app)




# models below
class User(db.Model):
    '''User'''

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,)
                    
    first_name = db.Column(db.String(50), nullable=False, unique=False)

    last_name = db.Column(db.String(50), nullable=False, unique=False)

    image_url = db.Column(db.String(150), nullable=True)


class Post(db.Model):


    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,)

    title = db.Column(db.String(50), nullable=False, unique=False)
    
    content = db.Column(db.String(), nullable=False, unique=False)
    
    created_at = db.Column(db.String(), nullable=False, unique=False)

    user_key = db.Column(db.Integer, db.ForeignKey('user.id'))

    

class Tag(db.Model):

    __tablename__ = 'tag'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,)

    title = db.Column(db.String(50), nullable=False, unique=False)


class PostTag(db.Model):


    __tablename__ = 'posttag'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,)

    post_id = db.Column(db.Integer, db.ForeignKey('post.id') )

    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))

    
