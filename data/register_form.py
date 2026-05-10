from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя и Фамилия', validators=[DataRequired()])
    status = SelectField(
        'Статус',
        choices=[('teacher', 'Учитель'), ('student', 'Ученик')],
        validators=[DataRequired()]
    )
    teacher_password = PasswordField('Пароль учителя')
    submit = SubmitField('Подтвердить')
