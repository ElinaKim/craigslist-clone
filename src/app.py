from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

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

    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def __repr__(self):
        return "<User '{}'>".format(self.username)

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(70), unique=True, nullable=False)
    parent_category_id = db.Column(db.Integer(), db.ForeignKey('category.id'), nullable=False)

    sub_categories = db.relationship('Category', remote_side=[id], backref='parent_category')

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"


if __name__ == '__main__':
    app.run()