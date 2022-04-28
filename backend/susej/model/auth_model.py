import datetime
from datetime import datetime

from flask_migrate import Migrate
from flask_restx import fields
from sqlalchemy_serializer import SerializerMixin
from susej.extension.database import db

migrate = Migrate()


class User(db.Model, SerializerMixin):
    __tablename__ = 'USERS'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.Text(), nullable=False)
    creation_date = db.Column(
        db.DateTime, nullable=False, default=datetime.now())

    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password

    def __repr__(self) -> str:
        return f"Login {self.email}"


class UserSchema(object):
    def __init__(self, api) -> None:
        self.api = api

    def user_schema(self):
        return self.api.model(
            'user', {
                "email": fields.String(description=u'Inserir e-mail para cadastro', required=True),
                "password": fields.String(description=u'Inserir senha para acesso a conta', required=True)
            }
        )


def init_app(app):
    migrate.init_app(app, db)
