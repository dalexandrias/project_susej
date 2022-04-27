from susej.constants.status_return import CREATED_USER, EMAIL_INVALID, ERROR, SUCCESS, EMAIL_ALREADY_EXISTS
from typing import Any
from flask import jsonify
from werkzeug.security import check_password_hash, generate_password_hash
import validators
from susej.commands_dml.commands import insert_table

from susej.model.login import User


class AuthService():
    def __init__(self) -> None:
        pass
    
    def save_new_user(new_user: User) -> jsonify:
        user = User.query.filter_by(email=new_user.email).first()
        if not user:
            if validators.email(new_user.email):
                insert_table(new_user)
                return jsonify(
                    {
                        "status": SUCCESS,
                        "mensage": CREATED_USER
                    }
                ), 201
            else:
                return jsonify(
                    {
                        "status": ERROR,
                        "mensage": EMAIL_INVALID
                    }
                )
        else:
            return jsonify(
                {
                    "status": ERROR,
                    "mensage": EMAIL_ALREADY_EXISTS
                }
            )
