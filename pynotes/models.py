from pynotes import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    nota = database.relationship("Nota", backref="usuario", lazy=True)

class Nota(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nota = database.Column(database.String, default="Olá pyNotes 3.0")
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'),  nullable=False)
