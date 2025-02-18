from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import sqlalchemy as sa
from app import db
from app.models import User

class LoginForm(FlaskForm):
  username = StringField('Логин', validators=[DataRequired()])
  password = PasswordField('Пароль', validators=[DataRequired()])
  remember_me = BooleanField('Запомнить меня')
  submit = SubmitField('Авторизация')

class RegistrationForm(FlaskForm):
  username = StringField('Логин', validators=[DataRequired()])
  email = StringField('Электронная почта', validators=[DataRequired(), Email()])
  password = PasswordField('Пароль', validators=[DataRequired()])
  password2 = PasswordField(
    'Повторите пароль ', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Регистрация')

  def validate_username(self, username):
    user = db.session.scalar(sa.select(User).where(
      User.username == username.data))
    if user is not None:
      raise ValidationError('используйте другое имя пользователя')

  def validate_email(self, email):
    user = db.session.scalar(sa.select(User).where(
      User.email == email.data))
    if user is not None:
      raise ValidationError('используйте другую электронную почту')

class CreatorForm(FlaskForm):
  name = StringField('Имя', validators=[DataRequired()])
  surname = StringField('Фамилия', validators=[DataRequired()])
  classes_dropdown_list = ['5а', '5б', '5в', '5г', '6а', '6б', '6в', '6г', '7а', '7б', '7в', '7г'] # You can get this from your model
  class = SelectField('Classes', choices=classes_dropdown_list, default=1)
  