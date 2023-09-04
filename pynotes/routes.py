from flask import render_template
from pynotes import app
from pynotes.forms import SignIn

@app.route('/')
def home():
    form = SignIn()
    return render_template('home.html', form=form)
