from flask import Blueprint, request
from flask_restx import Api, Resource

bp = Blueprint('client', __name__, url_prefix='/client/api/v1')
api = Api(bp, version='1.0', title='Client API', description='API para controle dos clientes')
client_ns = api.namespace('client', description='Controle do fluxo das operações para os clientes')


@client_ns.route('/')
class CreateClient(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)
        
    def post(self):
        client_in = request.get_json()

    def get(self):
        ...
        
    def put(self):
        ...
        
    def delete(self):
        ...
