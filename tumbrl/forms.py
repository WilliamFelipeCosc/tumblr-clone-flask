from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from tumbrl.models import User
from wtforms.widgets import TextArea


class FormLogin(FlaskForm):
    email = StringField('Email')
    password = PasswordField('Password')
    btn = SubmitField('Login')


class FormCreateNewAccount(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 25)])
    checkPassword = PasswordField('Confirmar Senha', validators=[DataRequired(), Length(6, 25), EqualTo('password')])
    btn = SubmitField('Criar conta')

    def validate_email(self, email):
        email_of_user = User.query.filter_by(email=email.data).first()
        if email_of_user:
            return ValidationError('Já existe um usuário com esse email')

class FormDeleteAccount(FlaskForm):
    btn = SubmitField('Deletar conta')


class FormCreateNewPost(FlaskForm):
    text = StringField('Título', widget=TextArea(), validators=[DataRequired()])
    photo = FileField('Anexar imagem', validators=[DataRequired()])
    btn = SubmitField('Publicar')


class FormLikePost(FlaskForm):
    like_btn = SubmitField('Like')
    dislike_btn = SubmitField('Dislike')
