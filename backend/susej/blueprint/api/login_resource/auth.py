from datetime import datetime

from flask import jsonify
from susej.commands_dml import commands as data_base
from flask_restful import Resource, reqparse
from susej.model.login import User
from susej.services.auth_services import AuthService


class CreateUser(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.auth_service = AuthService
        
    def post(self):
        try:
            body_parse = reqparse.RequestParser()
            body_parse.add_argument('email', type=str)
            body_parse.add_argument('password', type=str)
            args = body_parse.parse_args()
            
            user = User(**args)

            return self.auth_service.save_new_user(new_user=user)
        except Exception as error:
            return jsonify(
                {
                    "status": 0,
                    "mensage": "Error",
                    "decription": f"{error}"
                }
            )   
