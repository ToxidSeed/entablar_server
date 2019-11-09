from model.ModelCampo import ModelCampo
from domain.DomainCampo import DomainCampo
import json


class Campo:

    def __init__(self):
        self.model = ModelCampo()
        pass

    def guardar(self, data={}):
        obj = DomainCampo()
        obj.tabla_id                = data["tabla_id"]
        obj.campo_id                = data["campo_id"]
        obj.nombre                  = data["nombre"]
        obj.descripcion             = data["descripcion"]
        obj.flg_obligatorio       = data["flg_obligatorio"]
        obj.flg_pk                  = data["flg_pk"]
        obj.tipo_dato_id            = data["tipo_dato_id"]
        obj.tipo_dato_data = data["tipo_dato_data"]
        obj.tipo_dato_text = self.get_tipo_dato_text(data["tipo_dato_data"], data["tipo_dato_syntax"])
        obj.tipo_dato_syntax = data["tipo_dato_syntax"]

        if obj.campo_id != 0 and obj.campo_id != "":
            self.model.actualizar(obj)
        else:
            self.model.insertar(obj)
        return obj.__dict__

    def get_tipo_dato_text(self, data, syntax=""):
        tipo_dato_text_str = ''
        data_dict = json.loads(data)

        # Los datos se encuentran en el campo tipo_dato_data almacenado json
        for key, value in data_dict.items():
            if len(tipo_dato_text_str) == 0:
                tipo_dato_text_str = syntax

            param='%'+key
            tipo_dato_text_str = tipo_dato_text_str.replace(param, value)

        # Si los datos de precision no se encuentran en bd el texto sera el mismo que el de sintaxis
        if tipo_dato_text_str == "":
            tipo_dato_text_str = syntax

        return tipo_dato_text_str


    def get_campos_por_tabla(self, data={}):
        query_str = ModelCampo.get_query("campo_get_campos_por_tabla")
        params = (data["tabla_id"],)
        result_set = ModelCampo.execute_query(query_str, params)
        response = {
            "rows":result_set
        }
        return response

    def get_object(self, data={}):
        params = (data["campo_id"],)
        query_str = self.model.get_query("campo_get")
        obj = self.model.get_single_result(query_str, params)
        return obj
