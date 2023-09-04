from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from pynotes import Usuario

class signup(FlaskForm):
    email = StringField("Email", validators=[Email(), DataRequired()])
    username = StringField("Usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    confirmacao_senha =  PasswordField("Confirme a Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar Conta")

class signin(FlaskForm):
    email = StringField("Email", validators=[Email(), DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Login")
