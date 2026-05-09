from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, FieldList
from wtforms.validators import DataRequired


class AddTaskForm(FlaskForm):
    homework = StringField('Домашнее задание', validators=[DataRequired()])
    teacher = StringField('ID Учителя', validators=[DataRequired()])
    students = StringField('ID Учеников(оставить пустым, если задание для всех)')
    subject = StringField('Предмет ID', validators=[DataRequired()])
    date = StringField('Срок сдачи', validators=[DataRequired()])
    submit = SubmitField('Submit')