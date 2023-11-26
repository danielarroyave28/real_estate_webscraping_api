from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models.projects_model import Proyecto
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("Projects", "projects", description="Operations on projects")

@blp.route("/projects")
class ProjectList(MethodView):
    
    def get(self):
        projects_data = Proyecto.query.all()
        projects_dict = [p.to_dict() for p in projects_data]

        return projects_dict


@blp.route("/projects/<int:ciudad_id>")
class ProjectFilterByCiudad(MethodView):
    
    def get(self, ciudad_id):
        pass

@blp.route("/projects/<int:barrio_id>")
class ProjectFilterByBarrio(MethodView):

    def get(self, barrio_id):
        pass


    
    