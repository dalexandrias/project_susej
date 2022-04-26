from flask import Blueprint
from flask_restful import Api
from .resource import ProductService

bp = Blueprint("api", __name__, url_prefix='/api/v1')
api = Api(bp)

def init_app(app):
    api.add_resource(ProductService, "/product/")
    app.register_blueprint(bp)
