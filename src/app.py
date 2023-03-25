from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Hello World"

if __name__ == '__main__':
    app.run()