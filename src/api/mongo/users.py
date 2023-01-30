# src/api/users.py

from flask_restx import Resource, Api, fields
from flask import Blueprint, flash, url_for, render_template, request, redirect, make_response, session
from functools import wraps

from src import db, bcrypt
from .models import User
from .rdbms.users.forms import User_register, User_login

users = Blueprint('users', __name__, url_prefix="/user")

api = Api(users)


# new
user = api.model('User', {
    'id': fields.Integer(readOnly=True),
    'username': fields.String(required=True),
    'email': fields.String(required=True),
    'password': fields.String(required=True),
})


@api.route('/register')
class RegisterApi(Resource):
    @api.expect(user, validate=True)
    def post(self):
        form = User_register()
        post_data = request.get_json()
        username = post_data.get('username')
        email = post_data.get('email')
        password = post_data.get('password')
        hashed_password = bcrypt.generate_password_hash(
            password).decode('utf-8')

        user: User = User.get_byEmail(email)

        if user != None:
            flash(f'Email already exists!', 'danger')
            return make_response(redirect(url_for('users.login')))
        db.insert_single_user(
            User(username=username, email=email, password=hashed_password))
        flash(f'Account Created Successfully! ID:{id}', 'success')
        return make_response(render_template('register.html', title='Register', form=form))

    # @api.marshal_with(user, as_list=True)
    # def get(self):
    #     return User.get_all(), 200


@api.route('/login')
class LoginApi(Resource):
    def get(self, id=None, range=None, emotion=None):
        data = []
    def post(self):
        form = User_login()
        post_data = request.get_json()
        email = post_data.get('email')
        user: User = User.get_byEmail(email)
        authorized = bcrypt.check_password_hash(
            user.password, post_data.get('password'))
        if user:
            if authorized:
                session['logged_in'] = True
                session['user_id'] = user.id
                session['username'] = user.username
                flash('You have been logged in!', 'success')
                return make_response(redirect(url_for('index.home')))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
        return make_response(render_template('login.html', title='Login', form=form))

    def is_logged_in(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            if 'logged_in' in session:
                return f(*args, **kwargs)
            else:
                flash('Unauthorized, Please login', 'danger')
                return make_response(redirect(url_for('users.login')))
        return wrap

    @is_logged_in
    def logout():
        session.clear()
        flash('You are now logged out', 'success')
        return make_response(redirect(url_for('index.home')))


class UserCollc(Resource):

    @api.marshal_with(user)
    def get(self, user_id):
        user = User.get_byID(user_id)
        if not user:
            api.abort(404, f"User {user_id} does not exist")
        return user, 200


api.add_resource(RegisterApi, '/users')
api.add_resource(UserCollc, '/users/<int:user_id>')
