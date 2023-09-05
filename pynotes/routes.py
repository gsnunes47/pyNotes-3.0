from flask import render_template
from pynotes import app, bcrypt, database
from pynotes.forms import SignIn, SignUp
from pynotes.models import Usuario

@app.route('/', methods=['GET', 'POST'])
def home():
    form = SignIn()
    return render_template('home.html', form=form)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = SignUp()
    if form.is_submitted():
        senha = bcrypt.generate_password_hash(form.senha.data)
        user = Usuario(email=form.email.data, username=form.username.data, senha=senha)
        database.session.add(user)
        database.session.commit()
    return render_template('cadastro.html', form=form)
