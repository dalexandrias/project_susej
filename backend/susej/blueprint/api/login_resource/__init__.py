from flask import Blueprint, Flask
from flask_restful import Api
from .resource import CreateUser

bp = Blueprint('login', __name__, url_prefix='/api')
api = Api(bp)

def init_app(app: Flask):
    api.add_resource(CreateUser, '/login')
    app.register_blueprint(bp)
