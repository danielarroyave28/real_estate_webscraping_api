from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models.barrio_model import Barrio
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("Barrios", "barrios", description="Operations on barrios")

@blp.route("/barrios")
class ProjectList(MethodView):
    
    def get(self):
        barrios_data = Barrio.query.all()
        #projects_dict = [p.to_dict() for p in projects_data]
        barrios_dict = [p.to_dict() for p in barrios_data]

        return barrios_dict