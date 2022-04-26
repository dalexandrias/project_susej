from datetime import datetime
from susej.commands_dml import commands as data_base
from flask_restful import Resource, reqparse
from susej.model.login import User


class CreateUser(Resource):
    def post(self):
        body_parse = reqparse.RequestParser()
        body_parse.add_argument('email', type=str)
        body_parse.add_argument('password', type=str)
        args = body_parse.parse_args()
        
        login = User(**args, creation_date=datetime.now())
        
        data_base.insert_table(login)
        
        return login.to_dict()