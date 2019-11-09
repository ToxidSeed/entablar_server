from model.ModelTipoDato import ModelTipoDato
from domain.DomainTipoDato import DomainTipoDato
import os, json, re, ast


class TipoDato:

    def __init__(self):
        self.model = ModelTipoDato()

    def guardar(self, data={}):
        obj = DomainTipoDato()
        obj.tipo_dato_id = data["id"]
        obj.nombre = data['nombre']
        obj.descripcion = data['descripcion']
        obj.proveedor_bd_id = data['proveedor_bd_id']
        obj.config = data['config']

        if obj.tipo_dato_id != 0 and obj.tipo_dato_id != "" :
            self.model.actualizar(obj)
        else:
            self.model.insertar(obj)
        return obj.__dict__

    def get_proveedor(self, data={}):
        params = (data["proveedor_bd_id"],)
        query_str = self.model.get_query("proveedor_bd_get")
        result_set = self.model.execute_query(query_str, params)
        response = {}
        if len(result_set) == 1:
            response = result_set[0]

        return response

    def get_object(self, data={}):
        params = (data["tipo_dato_id"],)
        query_str = self.model.get_query("tipo_dato_get")
        result_set = self.model.execute_query(query_str, params)
        response = {}
        if len(result_set) == 1:
            response = result_set[0]
            response['config_json'] = self.get_config_as_json(response['config'])

        return response

    def get_list(self, data={}):
        query_str = self.model.get_query("tipo_dato_get_list")
        params = (data['dbms_id'], '%' + data["tipo_dato_nombre"] + '%',)
        result_set = self.model.execute_query(query_str, params)

        """records = []"""
        for elem in result_set:
            elem['config_json'] = self.get_config_as_json(elem['config'])

        response = {
            "rows": result_set
        }
        return response

    def get_config_as_json(self, config_str=""):
        elements_json = ""
        if config_str != "":
            params = config_str.split('\n')
            elements = []
            for config in params:
                elem = {}
                elem['param_name'] = re.search('^[a-zA-Z]+',config).group()
                elem['label'] = re.search('(?<=\()[a-zA-Z]+(?=\))',config).group()
                elem['inicio'] = re.search('(?<=inicio:)\s*[0-9]+',config).group()
                elem['fin'] = re.search('(?<=fin:)\s*[0-9]+', config).group()
                elements.append(elem)
            elements_json = json.dumps(elements)

        return elements_json



