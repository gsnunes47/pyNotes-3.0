from flask import render_template, redirect, url_for
from pynotes import app, bcrypt, database
from pynotes.forms import SignIn, SignUp, Note
from pynotes.models import Usuario, Nota
from datetime import datetime
from flask_login import login_required, login_user, logout_user, current_user

@app.route('/', methods=['GET', 'POST'])
def home():
    form = SignIn()
    if form.is_submitted():
        user = Usuario.query.filter_by(email=form.login.data).first()
        senha = bcrypt.check_password_hash(user.senha, form.senha.data)
        if user and senha:
            login_user(user)
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
        login_user(user)
        return redirect(url_for('perfil', id_usuario=user.id))
    return render_template('cadastro.html', form=form)

@app.route('/perfil/<id_usuario>', methods=['GET', 'POST'])
@login_required
def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id):
        form = Note()
        user = Usuario.query.get(int(id_usuario))
        if form.is_submitted():
            note = Nota(nota=form.texto.data, id_usuario=user.id, data_criacao=datetime.utcnow())
            database.session.add(note)
            database.session.commit()
        return render_template("perfil.html", user=user, form=form, notes=user.nota)
    else:
        user = Usuario.query.get(int(id_usuario))
        return render_template("perfil.html", user=user, form=None, notes=user.nota)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/feed')
@login_required
def feed():
    notas = Nota.query.order_by(Nota.data_criacao).all()
    user = Usuario()
    return render_template('feed.html', notas=notas, user=user)
