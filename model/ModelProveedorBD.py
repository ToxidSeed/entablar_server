from model.BaseModel import BaseModel


class ModelProveedorBD(BaseModel):
    def __init__(self):
        pass

    def insertar(self, obj=None):
        stmt = BaseModel.get_query("proveedor_bd_insert")
        """now = datetime.datetime.now()
        obj.fch_creacion = now
        fch_creacion = str(now.strftime("%Y-%m-%d"))"""
        insert_data = (
            obj.nombre,
            obj.icono
        )
        obj.proveedor_bd_id = self.execute_insert(stmt, insert_data)
