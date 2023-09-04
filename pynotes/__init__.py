from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dados.db"
app.config["SECRET_KEY"] = "c401f29fac31b7c2972f29d97a4f37c6"

database = SQLAlchemy(app)

from pynotes import routes
