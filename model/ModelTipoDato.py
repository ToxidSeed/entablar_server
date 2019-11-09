from model.BaseModel import  BaseModel
from domain.DomainTipoDato import DomainTipoDato

class ModelTipoDato(BaseModel):
    def __init__(self):
        pass

    def insertar(self, obj=None):
        stmt = BaseModel.get_query("tipo_dato_insert")

        list_data = list(obj.__dict__.values())
        list_data.pop(0)
        insert_data = tuple(list_data)
        obj.tipo_dato_id = self.execute_insert(stmt, insert_data)

    def actualizar(self, obj=None):
        stmt = BaseModel.get_query("tipo_dato_actualizar")
        self.execute_update(stmt, obj.__dict__)
