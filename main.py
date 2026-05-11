import time
from flask import Flask, render_template
from flask_login import LoginManager, current_user


from data.db_session import global_init, create_session
from data.users import User
from data.user_api import user_blueprint
from data.homeworks import Hometask
from data.job_api import hometask_blueprint


app = Flask(__name__)
app.register_blueprint(user_blueprint)
app.register_blueprint(hometask_blueprint)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


# Основное
@login_manager.user_loader
def load_user(user_id):
    db_sess = create_session()
    return db_sess.query(User).get(user_id)

@app.route('/')
def index():
    db_sess = create_session()
    now = time.time()
    jobs = []
    for job in db_sess.query(Hometask).all():
        if current_user.is_authenticated and current_user.status == 'teacher':
            if str(job.teacher) != str(current_user.id):
                continue
            jobs.append(job)
            continue

        try:
            deadline = time.mktime(time.strptime(str(job.date).strip(), '%d.%m.%Y'))
        except (TypeError, ValueError, OverflowError):
            continue

        is_public = job.students in (None, '', 0, '0')
        days_before = 7 if is_public else 14
        seconds_left = deadline - now

        if seconds_left < 0 or seconds_left > days_before * 24 * 60 * 60:
            continue

        if is_public:
            jobs.append(job)
            continue

        if not current_user.is_authenticated:
            continue

        current_user_id = str(current_user.id)
        if current_user_id in (str(job.students), str(job.teacher)):
            jobs.append(job)

    users = db_sess.query(User).all()
    names = {name.id: (name.name) for name in users}
    return render_template('index.html', names=names, jobs=jobs, title='Homeworks FOREVER')


def main():
    global_init('db/homework_site.sqlite')
    app.run()


if __name__ == '__main__':
    main()
