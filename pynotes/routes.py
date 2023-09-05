from flask import render_template, redirect, url_for
from pynotes import app, bcrypt, database
from pynotes.forms import SignIn, SignUp
from pynotes.models import Usuario

@app.route('/', methods=['GET', 'POST'])
def home():
    form = SignIn()
    if form.is_submitted():
        user = Usuario.query.filter_by(email=form.login.data).first()
        senha = bcrypt.check_password_hash(user.senha, form.senha.data)
        if user and senha:
            return redirect(url_for("perfil", id_usuario=user.id))
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

@app.route('/perfil/<id_usuario>')
def perfil(id_usuario):
    user = Usuario.query.get(int(id_usuario))
    return render_template("perfil.html", user=user)
