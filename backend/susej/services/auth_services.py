from http import HTTPStatus

import validators
from flask import jsonify
from susej.commands_dml.commands import insert_table, update_table
from susej.constants.status_return import (CREATED_USER, EMAIL_ALREADY_EXISTS,
                                           EMAIL_INVALID, EMAIL_NOT_REGISTER,
                                           EMAIL_UPDATED, ERROR,
                                           NEW_EMAIL_ALREADY_EXISTS, SUCCESS)
from susej.model.auth_model import User
from werkzeug.security import check_password_hash, generate_password_hash


class AuthService():
    def __init__(self) -> None:
        pass

    def save_user(self, new_user: User) -> jsonify:
        user = new_user.query.filter_by(email=new_user.email).first()
        if not user:
            if validators.email(new_user.email):

                new_user.password = generate_password_hash(new_user.password)

                insert_table(new_user)

                return {
                    "status": SUCCESS,
                    "message": CREATED_USER
                }, HTTPStatus.CREATED
            else:
                return {
                    "status": ERROR,
                    "message": EMAIL_INVALID
                }, HTTPStatus.BAD_REQUEST

        else:
            return {
                "status": ERROR,
                "message": EMAIL_ALREADY_EXISTS
            }, HTTPStatus.BAD_REQUEST

    def user_update(self, update_user: dict) -> User:
        user_current = User.query.filter_by(email=update_user['email']).first()

        if user_current:
            new_email = User.query.filter_by(
                email=update_user['new_email']).first()

            if not new_email:
                user_current.email = update_user['new_email']
                user_current.password = generate_password_hash(
                    update_user['password'])

                update_table()

                return {
                    "status": SUCCESS,
                    "message": EMAIL_UPDATED
                }, HTTPStatus.OK
            else:
                return {
                    "status": ERROR,
                    "message": NEW_EMAIL_ALREADY_EXISTS
                }, HTTPStatus.BAD_REQUEST

        else:
            return {
                "status": ERROR,
                "message": EMAIL_NOT_REGISTER
            }, HTTPStatus.BAD_REQUEST
