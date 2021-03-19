from app import db

class TipoDato(db.Model):
    __tablename__ = 'tipo_dato'
    tipo_dato_id = db.Column(db.Integer, primary_key=True)
    proveedor_bd_id = db.Column(db.Integer)
    nombre = db.Column(db.String(45))
    descripcion = db.Column(db.String(100))
    config = db.Column(db.String(1000))
    