from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig
from datetime import datetime

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Hello World"

class User(db.Model):
    __tablename__ = 'my_users'
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(65), unique=True)
    email = db.Column(db.String(120), unique=True)
    listings = db.relationship('Listing', backref='listing', lazy='dynamic')

    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def __repr__(self):
        return "<User '{}'>".format(self.username)
    
class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(70), unique=True, nullable=False)
    parent_category_id = db.Column(db.Integer(), db.ForeignKey('category.id'))

    sub_categories = db.relationship('Category', remote_side=[id], backref='parent_category')

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"

listing_category = db.Table('listing_category', db.Column('listing_id', db.Integer(), db.ForeignKey('listing.id')),
db.Column('category_id', db.Integer(), db.ForeignKey('category.id')))

class Listing(db.Model):
    __tablename__ = 'listing'
    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    date_update = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('my_users.id'))
    categories = db.relationship('Category', secondary='listing_category', backref=db.backref('listings', lazy='dynamic'))


if __name__ == '__main__':
    app.run()