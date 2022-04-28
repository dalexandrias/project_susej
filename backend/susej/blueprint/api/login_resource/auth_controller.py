from http import HTTPStatus

from flask import Blueprint, Flask, jsonify
from flask_restx import Api, Resource, reqparse
from susej.model.auth_model import User, UserSchema
from susej.services.auth_services import AuthService

bp = Blueprint('auth', __name__, url_prefix='/api')
api = Api(bp, version='1.0', title='Auth API', description='API controle dos usuarios')
auth_ns = api.namespace('auth', description='Autenticação dos usuarios')
user_schema = UserSchema(api).user_schema()

@auth_ns.route('/newuser')
class CreateUser(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)
        self.auth_service = AuthService
        
    # @auth_ns.route('newuser', method=['POST'])
    @auth_ns.expect(user_schema, validate=True)
    def post(self):
        try:
            body_parse = reqparse.RequestParser()
            body_parse.add_argument('email', type=str)
            body_parse.add_argument('password', type=str)
            args = body_parse.parse_args()

            user = User(**args)

            return self.auth_service.new_user(new_user=user)
        except Exception as error:
            response = jsonify(
                {
                    "status": 0,
                    "mensage": "Error",
                    "decription": f"{error}"
                }
            )
            response.status_code = HTTPStatus.BAD_REQUEST
            return response

    def put(self):
        try:
            ...

        except Exception as error:
            response = jsonify(
                {
                    "status": 0,
                    "mensage": "Error",
                    "decription": f"{error}"
                }
            )
            response.status_code = HTTPStatus.BAD_REQUEST
            return response
