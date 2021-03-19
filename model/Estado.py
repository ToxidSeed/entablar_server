from app import db

class Estado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_estado_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))