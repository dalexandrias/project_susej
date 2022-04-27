import datetime
from email.policy import default
from enum import unique

from susej.extension.database import db
from sqlalchemy_serializer import SerializerMixin
from flask_migrate import Migrate
from datetime import datetime


migrate = Migrate()

class User(db.Model, SerializerMixin):
    __tablename__ = 'USERS'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.Text(), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password
        
    def __repr__(self) -> str:
        return f"Login {self.email}"


def init_app(app):
    migrate.init_app(app, db)
