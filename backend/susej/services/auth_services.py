from susej.constants.status_return import CREATED_USER, EMAIL_INVALID, ERROR, SUCCESS, EMAIL_ALREADY_EXISTS
from flask import jsonify
from http import HTTPStatus
from werkzeug.security import check_password_hash, generate_password_hash
import validators
from susej.commands_dml.commands import insert_table

from susej.model.login import User


class AuthService():
    def __init__(self) -> None:
        pass
    
    def new_user(new_user: User) -> jsonify:
        user = new_user.query.filter_by(email=new_user.email).first()
        if not user:
            if validators.email(new_user.email):
                
                new_user.password = generate_password_hash(new_user.password)
                
                insert_table(new_user)
                
                response = jsonify(
                    {
                        "status": SUCCESS,
                        "mensage": CREATED_USER
                    }
                )
                response.status_code = HTTPStatus.CREATED
                
                return response
            else:
                response = jsonify(
                    {
                        "status": ERROR,
                        "mensage": EMAIL_INVALID
                    }
                )
                response.status_code = HTTPStatus.BAD_REQUEST
                
                return response
        else:
            response = jsonify(
                {
                    "status": ERROR,
                    "mensage": EMAIL_ALREADY_EXISTS
                }
            )
            response.status_code = HTTPStatus.BAD_REQUEST
            
            return response
