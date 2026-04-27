from flask import Flask, render_template
from flask_login import LoginManager, login_user, login_required, logout_user


from .data.db_session import global_init, create_session
from .data.users import User
from .data.user_api import user_blueprint


app = Flask(__name__)
app.register_blueprint(user_blueprint)
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
    users = db_sess.query(User).all()
    names = {name.id: (name.surname, name.name) for name in users}
    return render_template('index.html', names=names, title='Work log')


def main():
    global_init('bd/homework_site.sqlite')
    app.run()


if __name__ == '__main__':
    main()