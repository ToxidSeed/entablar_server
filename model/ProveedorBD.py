from app import db

class ProveedorBD(db.Model):
    __tablename__ = 'proveedor_bd'
    proveedor_bd_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45))    
    icono = db.Column(db.String(100))
    