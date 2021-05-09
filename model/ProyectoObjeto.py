from app import db

class ProyectoObjeto(db.Model):
    __tablename__ = 'proyecto_objeto'
    id = db.Column(db.Integer, primary_key=True)
    proyecto_id = db.Column(db.Integer)
    objeto_id = db.Column(db.Integer)
    locked = db.Column(db.Integer)