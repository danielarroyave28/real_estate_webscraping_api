from db import db

class Ciudad(db.Model):
    __tablename__ = 'ciudad'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, unique=True)
    
    proyectos = db.relationship('Proyecto', back_populates='ciudad')

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.name
        }