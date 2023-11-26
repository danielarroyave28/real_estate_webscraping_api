from flask import Flask, jsonify
from flask_smorest import Api
from flask_migrate import Migrate
from flask_cors import CORS
from db import db
import models


from resources.new_projects import blp as ProyectBlueprint
from resources.ciudades import blp as CiudadBlueprint
from resources.barrios import blp as BarrioBlueprint


def create_app():
    app = Flask(__name__)

    #CORS(app)

    # Configure the database connection URI
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Real Estate Projects REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///informeinmobiliario.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)


    migrate = Migrate(app,db)

    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(ProyectBlueprint)
    api.register_blueprint(CiudadBlueprint)
    api.register_blueprint(BarrioBlueprint)
    

    return app