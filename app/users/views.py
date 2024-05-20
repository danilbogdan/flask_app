import flask
from flask.views import View, MethodView
from werkzeug.security import check_password_hash, generate_password_hash

from app import app
from app.users.models import User
from app.database import db
from app.users.forms import UserForm


@app.get('/users')
def list_users():
    users = User.query.all()
    return flask.render_template('users/list_users.html', users=users)


@app.route('/users/create', methods=['GET', 'POST'])
def create_user():
    form = UserForm()
    if flask.request.method == 'GET':
        return flask.render_template('users/create_user.html',  form=form)
    elif flask.request.method == 'POST':
        user = User()
        form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return flask.redirect(flask.url_for('login'))



@app.get('/users/<int:user_id>')
def get_user(user_id):
    if 'username' not in flask.session:
        return flask.redirect(flask.url_for('login'))
    return flask.render_template('users/user_details.html', user_id=user_id)


# user login view
@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return flask.render_template('users/login.html')
    elif flask.request.method == 'POST':
        username = flask.request.form.get('username')
        password = flask.request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user.password == password:
            flask.session['username'] = username
            flask.session['user_id'] = user.id
            return flask.redirect(flask.url_for('get_user', user_id=1))
        else:
            return flask.render_template('users/login.html', error='Wrong username or password')


@app.route('/logout')
def logout():
    flask.session.pop('username', None)
    return flask.redirect(flask.url_for('login'))



class UserListView(View):
    methods = ['GET', 'POST']
    def __init__(self, model, template):
        self.model = model
        self.template = template

    def dispatch_request(self):
        users = self.model.query.all()
        return flask.render_template(self.template, users=users)

class UserView(MethodView):
    def __init__(self, model):
        self.model = model

    def get(self, user_id):
        return f'<h1> User id: {user_id}'

    def patch(self, user_id):
        return f'<h1> User updated: {user_id}'


app.add_url_rule(
    '/v2/list_users/',
    view_func=UserListView.as_view('list_users_v2', User, 'users/list_users_v2.html')
)
app.add_url_rule(
    '/v2/user/<int:user_id>',
    view_func=UserView.as_view('read_update_user_v2', model=User)
)
