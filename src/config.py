from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    conn_str  = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    debug = True 
    SQLALCHEMY_DATABASE_URI  = Config.conn_str