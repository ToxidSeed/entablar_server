from app import db

class ProyectoUsuario(db.Model):
    __tablename__ = 'proyecto_usuario'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer)
    proyecto_id = db.Column(db.Integer)
