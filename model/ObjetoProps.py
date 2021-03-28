from app import db

class ObjetoProps(db.Model):
    __tablename__ = "objeto_props"
    id = db.Column(db.Integer, primary_key=True)
    objeto_id = db.Column(db.Integer)
    nombre = db.Column(db.String(50))
    valor = db.Column(db.String(250))
    flg_activo = db.Column(db.String(1))
    fch_creacion = db.Column(db.Date)
    fch_modificacion = db.Column(db.Date)
