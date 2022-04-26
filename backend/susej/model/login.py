import datetime

from susej.extension.database import db
from sqlalchemy_serializer import SerializerMixin
from flask_migrate import Migrate


migrate = Migrate()

class User(db.Model, SerializerMixin):
    __tablename__ = 'USERS'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, email: str, password: str, creation_date: datetime.datetime) -> None:
        self.email = email
        self.password = password
        self.creation_date = creation_date
        
    def __repr__(self) -> str:
        return f"Login {self.email}"
    

def init_app(app):
    migrate.init_app(app, db)
