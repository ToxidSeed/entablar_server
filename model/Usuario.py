from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    password = db.Column(db.String(100))
    descripcion = db.Column(db.String(250))
    email = db.Column(db.String(200))
    provider = db.Column(db.String(20))
    fch_creacion = db.Column(db.Date)
    confirmado = db.Column(db.SmallInteger)
    fch_confirmacion = db.Column(db.Date)
