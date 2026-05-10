import flask
from flask_login import current_user, login_required

from . import db_session
from .addhome import AddTaskForm
from .users import User
from data.homeworks import Hometask

hometask_blueprint = flask.Blueprint(
    'hometask_api',
    __name__,
    template_folder='templates'
)


@hometask_blueprint.route('/addhometask', methods=['GET', 'POST'])
@login_required
def add_job():
    if current_user.status != 'teacher':
        return flask.redirect('/')

    db_sess = db_session.create_session()
    form = AddTaskForm()
    students = db_sess.query(User).filter(User.status == 'student').order_by(User.name).all()
    form.students.choices = [(0, 'Для всех учеников')] + [
        (student.id, f'{student.name} (ID: {student.id})') for student in students
    ]

    if form.validate_on_submit():
        hometask = Hometask(
            homework=form.homework.data,
            teacher=current_user.id,
            students=form.students.data or None,
            subject=form.subject.data,
            date=form.date.data
        )
        db_sess.add(hometask)
        db_sess.commit()
        return flask.redirect('/')

    return flask.render_template(
        'addtask.html',
        title='Добавление работы',
        form=form,
        teacher_name=current_user.name
    )
