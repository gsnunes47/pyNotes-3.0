from pynotes import database, app
from pynotes.models import Usuario, Nota

with app.app_context():
    database.create_all()
