from db import db

class Barrio(db.Model):
    __tablename__ = 'barrio'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.name
        }