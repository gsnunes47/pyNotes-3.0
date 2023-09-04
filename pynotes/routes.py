from flask import render_template
from pynotes import app
from pynotes.forms import SignIn, SignUp

@app.route('/', methods=['GET', 'POST'])
def home():
    form = SignIn()
    return render_template('home.html', form=form)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = SignUp()
    return render_template('cadastro.html', form=form)
