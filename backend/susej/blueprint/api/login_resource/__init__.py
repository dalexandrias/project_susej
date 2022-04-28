from flask import Flask
from susej.blueprint.api.login_resource.auth_controller import bp


def init_app(app: Flask):
    # api.add_resource(CreateUser, '/login')
    app.register_blueprint(bp)
