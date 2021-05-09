from app import db

class TipoObjeto(db.Model):
    __tablename__="tipo_objeto"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    icono = db.Column(db.String(100))
    fch_creacion = db.Column(db.Date)