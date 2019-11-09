from model.BaseModel import BaseModel
from domain.DomainTabla import DomainTabla
import datetime
from datetime import date


class ModelTabla(BaseModel):
    def __init__(self):
        pass

    def insertar(self, obj=None):
        stmt = BaseModel.get_query("tabla_insert")

        now = datetime.datetime.now()
        #Convert to iso format to insert
        #obj.fch_registro =  str(now.strftime("%Y-%m-%d"))
        obj.fch_creacion = now
        fch_creacion = str(now.strftime("%Y-%m-%d"))

        insert_data = (
                       obj.nombre,
                       obj.descripcion,
                       fch_creacion,
                       obj.dbms_id)

        obj.tabla_id = self.execute_insert(stmt,insert_data)

    def actualizar(self, obj=None):
        stmt = BaseModel.get_query("tabla_actualizar")
        self.execute_update(stmt, obj.__dict__)




    def get_object(self, params):
        query_str = BaseModel.get_query("tabla_get_object")
        result_set = BaseModel.execute_query(query_str, params)
        obj = DomainTabla()
        if len(result_set) == 1:
            for element_dict in result_set:
                BaseModel.dict_to_object(obj, element_dict)

        return obj





