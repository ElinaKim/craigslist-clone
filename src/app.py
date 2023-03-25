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

    def __init__(self, username):
        self.username = username
    
    def __repr__(self):
        return "<User '{}'>".format(self.username)
    
if __name__ == '__main__':
    app.run()