from app import db

class Objeto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    tipo_objeto_id = db.Column(db.Integer)
    dbms_id = db.Column(db.Integer)
    #database_id = db.Column(db.Integer) 
    #esquema_id = db.Column(db.Integer)
    objeto_padre_id = db.Column(db.Integer)
    desc_abreviada = db.Column(db.String(250))
    desc_completa = db.Column(db.String(250))
    estado_id = db.Column(db.Integer)
    fch_creacion = db.Column(db.Date)
    fch_modificacion = db.Column(db.Date)
    