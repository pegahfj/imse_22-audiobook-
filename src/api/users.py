# src/api/users.py


from flask import Blueprint, request
from flask_restx import Resource, Api, fields 

from src import db
from .models import User


users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)

# new
user = api.model('User', {
    'id': fields.Integer(readOnly=True),
    'username': fields.String(required=True),
    'email': fields.String(required=True),
    'password': fields.String(required=True),
})


class UsersList(Resource):

    @api.expect(user, validate=True)  # new
    def post(self):
        post_data = request.get_json()
        username = post_data.get('username')
        email = post_data.get('email')
        password = post_data.get('password')
        response_object = {}

        user = User.get_byEmaily(email)
        if user:
            response_object['message'] = 'Sorry. That email already exists.'
            return response_object, 400

        db.insert_single_user(User(username=username, email=email, password=password))

        response_object['message'] = f'{email} was added!'
        return response_object, 201
    
    
    @api.marshal_with(user, as_list=True)
    def get(self):
        return User.get_all(), 200


class Users(Resource):

    @api.marshal_with(user)
    def get(self, user_id):
        user = User.get_byID(user_id)
        if not user:
            api.abort(404, f"User {user_id} does not exist")
        return user, 200

api.add_resource(UsersList, '/users')
api.add_resource(Users, '/users/<int:user_id>')