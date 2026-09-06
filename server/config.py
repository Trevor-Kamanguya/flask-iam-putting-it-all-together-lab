# Standard library imports

# Remote library imports
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.secret_key = b'\xdd\xe6\xdc\xf7\xf3\x88\x91\xc6\xb0\xbd\x8d\xe1'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)

bcrypt = Bcrypt(app)
api = Api(app)