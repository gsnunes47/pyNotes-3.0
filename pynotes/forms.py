from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

class SignUp(FlaskForm):
    email = StringField("Email", validators=[Email(), DataRequired()])
    username = StringField("Usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    confirmacao_senha =  PasswordField("Confirme a Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar Conta")

class SignIn(FlaskForm):
    login = StringField("Email", validators=[Email(), DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Login")

class Note(FlaskForm):
    texto = StringField("Escreva o que você esta pensando agora.", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Enviar")
    