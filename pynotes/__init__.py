from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dados.db"
app.config["SECRET_KEY"] = "c401f29fac31b7c2972f29d97a4f37c6"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from pynotes import routes
