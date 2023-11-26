from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models.ciudad_model import Ciudad
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("Ciudades", "ciudades", description="Operations on ciudades")

@blp.route("/ciudades")
class ProjectList(MethodView):
    
    def get(self):
        ciudades_data = Ciudad.query.all()
        #projects_dict = [p.to_dict() for p in projects_data]
        ciudades_dict = [p.to_dict() for p in ciudades_data]

        return ciudades_dict