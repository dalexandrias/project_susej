from flask_restx import Api, fields


class ClientSchemas(object):
    def __init__(self, api: Api) -> None:
        self.api = api
        
    def new_client(self):
        return self.api.model(
            'Client', {
                "nome": fields.String(description='Nome do Cliente', required=True),
                "sobrenome": fields.String(description='sobrenome do Cliente', required=True),
                "rua": fields.String(description='rua do Cliente', required=True),
                "bairro": fields.String(description='bairro do Cliente', required=True),
                "cidade": fields.String(description='cidade do Cliente', required=True),
                "estado": fields.String(description='estado do Cliente', required=True),
                "cep": fields.String(description='cep do Cliente', required=True),
            }
        )
