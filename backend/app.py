from flask import Flask

# from susej.extension import manager_login
from susej.blueprint.api import product_resource, login_resource
# from susej.blueprint.api.login_resource.auth_controller import CreateUser
from susej.extension import configuration, database
from susej.model import auth_model as migrate

app = Flask(__name__)
configuration.init_app(app)
database.init_app(app)
login_resource.init_app(app)
product_resource.init_app(app)
# manager_login.init_app(app)
# migrate.init_app(app)
