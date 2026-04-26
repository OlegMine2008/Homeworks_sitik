import flask

from . import db_session
from users import User
from register_form import RegisterForm

blueprint = flask.Blueprint(
    'user_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return flask.render_template('register.html', title='Register', form=form,
                                   message="Passwords don't match")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return flask.render_template('register.html', title='Register', form=form,
                                   message="This user already exists")
        user = User(
            name=form.name.data,
            status=form.status.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return flask.redirect('/login')
    return flask.render_template('register.html', title='Регистрация', form=form)