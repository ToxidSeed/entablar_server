from model.BaseModel import BaseModel
from domain.DomainCampo import DomainCampo
import datetime
from datetime import date

class ModelCampo(BaseModel):

    def __init__(self):
        pass

    def insertar(self, obj=None):

        stmt = BaseModel.get_query("campo_insert")
        now = datetime.datetime.now()
        obj.fch_creacion = now
        fch_creacion = str(now.strftime("%Y-%m-%d"))
        insert_data = (
                        obj.tabla_id,
                        obj.nombre,
                        obj.descripcion,
                        obj.flg_obligatorio,
                        obj.flg_pk,
                        fch_creacion,
                        obj.tipo_dato_id,
                        obj.tipo_dato_data,
                        obj.tipo_dato_text,
                        obj.tipo_dato_syntax
                    )

        obj.campo_id = self.execute_insert(stmt,insert_data)

    def actualizar(self, obj=None):
        stmt = BaseModel.get_query("campo_actualizar")
        self.execute_update(stmt, obj.__dict__)



