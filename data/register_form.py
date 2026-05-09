from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, EmailField, SelectField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя и Фамилия', validators=[DataRequired()])
    status = SelectField('Статус', choices=[('teacher', 'Учитель'), ('student', 'Ученик')], validators=[DataRequired()])
    submit = SubmitField('Подтвердить')