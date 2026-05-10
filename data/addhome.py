from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired


class AddTaskForm(FlaskForm):
    homework = StringField('Домашнее задание', validators=[DataRequired()])
    students = SelectField('Ученик', choices=[], coerce=int, default=0)
    subject = StringField('Предмет ID', validators=[DataRequired()])
    date = StringField('Срок сдачи', validators=[DataRequired()])
    submit = SubmitField('Подтвердить')
