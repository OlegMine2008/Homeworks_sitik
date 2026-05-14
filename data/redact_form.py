import time

from flask_wtf import FlaskForm
from wtforms import FileField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Regexp, ValidationError


class RedactTaskForm(FlaskForm):
    homework = StringField('Домашнее задание', validators=[DataRequired()])
    students = SelectField('Ученик', choices=[], coerce=int, default=0)
    date = StringField(
        'Срок сдачи',
        validators=[
            DataRequired(),
            Regexp(r'^\d{2}\.\d{2}\.\d{4}$', message='Введите дату в формате ДД.ММ.ГГГГ')
        ]
    )
    file = FileField('Файл')
    submit = SubmitField('Подтвердить')

    def validate_date(self, field):
        try:
            time.strptime(field.data.strip(), '%d.%m.%Y')
        except (TypeError, ValueError):
            raise ValidationError('Введите корректную дату в формате ДД.ММ.ГГГГ')
