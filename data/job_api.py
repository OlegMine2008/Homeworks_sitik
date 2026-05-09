import flask

from . import db_session
from data.homeworks import Hometask
from .addhome import AddTaskForm

hometask_blueprint = flask.Blueprint(
    'hometask_api',
    __name__,
    template_folder='templates'
)


@hometask_blueprint.route('/addhometask', methods=['GET', 'POST'])
def add_job():
    form = AddTaskForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = Hometask(
            homework=form.homework.data,
            teacher=form.teacher.data,
            students=form.students.data,
            subject=form.subject.data,
            date=form.date.data
        )
        db_sess.add(user)
        db_sess.commit()
        return flask.redirect('/')
    return flask.render_template('addtask.html', title='Добавление Работы', form=form)


# @blueprint.route('/hometasks')
# def json_jobs():
#     db_sess = db_session.create_session()
#     news = db_sess.query(Jobs).all()
#     return flask.jsonify(
#         {
#             'jobs':
#                 [item.to_dict(only=('job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'team_leader')) for item in news]
#         }
#     )


# # Более простой метод
# @blueprint.route('/jobs/<int:job_id>', methods=['GET'])
# def json_job(job_id):
#     try:
#         db_sess = db_session.create_session()
#         job = db_sess.get(Jobs, job_id)
#         if not job:
#             return flask.make_response(flask.jsonify({'error': 'Not Id or wrong Id'}))
#         return flask.jsonify(
#             {
#                 'jobs':
#                     job.to_dict(only=(
#                         'job', 
#                         'work_size', 
#                         'collaborators', 
#                         'start_date', 
#                         'end_date', 
#                         'is_finished', 
#                         'team_leader'))
#             }
#         )
#     except Exception:
#         return flask.make_response(flask.jsonify({'error': 'Not Id or wrong Id'}))