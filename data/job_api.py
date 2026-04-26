import flask

from data import db_session
from .jobs import Jobs
from .addjob import AddJobForm

blueprint = flask.Blueprint(
    'job_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/addjob', methods=['GET', 'POST'])
def add_job():
    form = AddJobForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = Jobs(
            job=form.job.data,
            team_leader=form.main_worker.data,
            collaborators=form.collaborators.data,
            work_size=form.work_size.data,
            is_finished=form.is_finished.data
        )
        db_sess.add(user)
        db_sess.commit()
        return flask.redirect('/')
    return flask.render_template('addjob.html', title='Добавление Работы', form=form)


@blueprint.route('/jobs')
def json_jobs():
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).all()
    return flask.jsonify(
        {
            'jobs':
                [item.to_dict(only=('job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'team_leader')) for item in news]
        }
    )


# Более простой метод
@blueprint.route('/jobs/<int:job_id>', methods=['GET'])
def json_job(job_id):
    try:
        db_sess = db_session.create_session()
        job = db_sess.get(Jobs, job_id)
        if not job:
            return flask.make_response(flask.jsonify({'error': 'Not Id or wrong Id'}))
        return flask.jsonify(
            {
                'jobs':
                    job.to_dict(only=(
                        'job', 
                        'work_size', 
                        'collaborators', 
                        'start_date', 
                        'end_date', 
                        'is_finished', 
                        'team_leader'))
            }
        )
    except Exception:
        return flask.make_response(flask.jsonify({'error': 'Not Id or wrong Id'}))