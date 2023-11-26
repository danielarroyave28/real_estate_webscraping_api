from db import db

class Proyecto(db.Model):
    __tablename__ = 'proyectos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.Text)
    tipo = db.Column(db.Text)
    ciudad = db.Column(db.Text)
    barrio = db.Column(db.Text)
    link = db.Column(db.String(255))
    precio = db.Column(db.String(255))
    area = db.Column(db.Float)
    entrega = db.Column(db.String(255))
    habitaciones = db.Column(db.String(255))
    cuarto_util = db.Column(db.Text)
    baños = db.Column(db.String(255))
    parqueaderos = db.Column(db.String(255))
    estudio = db.Column(db.String(255))

    #ciudad_id = db.Column(db.Integer, db.ForeignKey('ciudad.id'), nullable=True)
    #ciudad = db.relationship('Ciudad', back_populates="proyectos")

    #barrio_id = db.Column(db.Integer, db.ForeignKey('barrio.id'), nullable=True)
    #barrio = db.relationship('Barrio', back_populates="proyectos")
    

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'ciudad': self.ciudad,
            'barrio': self.barrio,
            'link': self.link,
            'precio': self.precio,
            'area': self.area,
            'entrega': self.entrega,
            'habitaciones': self.habitaciones,
            'cuarto_util': self.cuarto_util,
            'baños': self.baños,
            'parqueaderos': self.parqueaderos,
            'estudio': self.estudio
            }
    
    # Float calcualation of price