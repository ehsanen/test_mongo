from flask import Blueprint, request
from http import HTTPStatus

from constants import TOKEN, TOKEN_TYPE
from server.mod_user.schemas import create_user_schema
from server import db

mod_user = Blueprint('auth', __name__, url_prefix='/v1/users')


def _check_bearer_token(auth_header):
    if auth_header is None:
        return False
    if not auth_header.startswith(TOKEN_TYPE):
        return False
    token = auth_header[len(TOKEN_TYPE) + 1:]
    if token != TOKEN:
        return False
    return True


@mod_user.route('/createUser', methods=['POST'])
def create_user():
    if not _check_bearer_token(request.headers.get('Authorization')):
        return 'Invalid token', HTTPStatus.UNAUTHORIZED

    args = request.form
    errors = create_user_schema.validate(args)
    if errors:
        return errors, HTTPStatus.BAD_REQUEST

    username = args['username']
    password = args['password']
    age = int(args['age'])

    user_collection = db.user_collection
    if user_collection.find_one({"username": username}):
        return 'User already exists', HTTPStatus.OK

    user = {'username': username, 'password': password, 'age': age}

    user_id = user_collection.insert_one(user).inserted_id

    return f'User created successfully with ID {user_id}', HTTPStatus.OK
