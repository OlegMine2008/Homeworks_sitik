import flask
import os
from flask import send_from_directory, abort
from flask_login import current_user, login_required

from . import db_session
from .addhome import AddTaskForm
from .subject import Subject
from .users import User
from data.homeworks import Hometask

hometask_blueprint = flask.Blueprint(
    'hometask_api',
    __name__,
    template_folder='templates'
)
UPLOAD_FILES = os.path.join('static', 'uploads', 'homeworks')


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

    subjects = db_sess.query(Subject).order_by(Subject.name).all()
    form.subject.choices = [
        (subject.id, subject.name) for subject in subjects
    ]

    if form.validate_on_submit():
        file_path = None
        if form.file.data and getattr(form.file.data, 'filename', ''):
            os.makedirs(UPLOAD_FILES, exist_ok=True)
            original_name = os.path.basename(form.file.data.filename).strip()

            if original_name:
                save_path = os.path.join(UPLOAD_FILES, original_name)
                form.file.data.save(save_path)
                file_path = os.path.join('uploads', 'homeworks', original_name).replace('\\', '/')
            
            hometask = Hometask(
                homework=form.homework.data,
                teacher=current_user.id,
                students=form.students.data or None,
                subject=form.subject.data,
                date=form.date.data,
                file=file_path
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


@hometask_blueprint.route('/homeworks/<int:id>/file')
@login_required
def load_file(id):
    db_sess = db_session.create_session()
    hw = db_sess.query(Hometask).get(id)

    if not hw or not hw.file:
        abort(404)

    path = hw.file.replace('\\', '/')
    directory, filename = os.path.split(path)
    dir = os.path.join('static', directory)

    if not os.path.exists(os.path.join(dir, filename)):
        abort(404)

    return send_from_directory(dir, filename, as_attachment=True)