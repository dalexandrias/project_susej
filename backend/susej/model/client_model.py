from flask_migrate import Migrate
from sqlalchemy_serializer import SerializerMixin
from susej.extension.database import db

migrate = Migrate()


class Client(db.Model, SerializerMixin):
    __tablename__ = 'CLIENT'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(200), nullable=False)
    rua = db.Column(db.String(200), nullable=False)
    bairro = db.Column(db.String(200), nullable=False)
    cidade = db.Column(db.String(200), nullable=False)
    estado = db.Column(db.String(200), nullable=False)
    cep = db.Column(db.String(200), nullable=False)

    def __init__(
        self,
        nome: str,
        sobrenome: str,
        rua: str,
        bairro: str,
        cidade: str,
        estado: str,
        cep: str
    ) -> None:

        self.nome = nome
        self.sobrenome = sobrenome
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def __repr__(self) -> str:
        return f"Client {self.nome}"


def init_app(app):
    migrate.init_app(app, db)
