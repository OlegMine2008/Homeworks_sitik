from flask_wtf import FlaskForm
from wtforms import FileField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired


class AddTaskForm(FlaskForm):
    homework = StringField('Домашнее задание', validators=[DataRequired()])
    students = SelectField('Ученик', choices=[], coerce=int, default=0)
    subject = SelectField('Предмет', choices=[], coerce=int, validators=[DataRequired()])
    date = StringField('Срок сдачи', validators=[DataRequired()])
    file = FileField('Файл')
    submit = SubmitField('Подтвердить')
