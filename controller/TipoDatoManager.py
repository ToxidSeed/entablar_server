#from model.ModelTipoDato import ModelTipoDato
from model.TipoDato import TipoDato
from domain.DomainTipoDato import DomainTipoDato
from model.ProveedorBD import ProveedorBD
import os, json, re, ast
from app import db

from helper.Response import Response
from helper.Transformer import Transformer


class TipoDatoManager:

    def __init__(self):
        pass

    def guardar(self, data={}):        

        tipo_dato = TipoDato(
            proveedor_bd_id=data["dbms_id"],
            nombre=data["nombre"],
            descripcion=data["descripcion"],
            config=data["config"]
        )

        db.session.add(tipo_dato)
        db.session.commit()

        msg = "Se ha guardado el tipo de dato con código {}".format(tipo_dato.tipo_dato_id)

        return Response(msg=msg,input_data=tipo_dato).get()
    

    def new(self, data={}):
        dbms = ProveedorBD.query.filter(
            ProveedorBD.proveedor_bd_id == data["dbms_id"]
        ).one()

        return Response(input_data=dbms).get()
        

    def get(self, data={}):
        tipo_dato = TipoDato.query.filter(
            TipoDato.tipo_dato_id == data["tipo_dato_id"]
        ).one()

        dbms = ProveedorBD.query.filter(
            ProveedorBD.proveedor_bd_id == tipo_dato.proveedor_bd_id
        ).one()
        
        dbms_dict = Transformer(input_data=dbms).model_to_dict()

        resp = Response(input_data=tipo_dato)
        resp.add_extradata("dbms",dbms_dict)
        return resp.get()

    def get_list(self, data={}):

        tipo_dato_nombre = "%{}%".format(data["tipo_dato_nombre"])
        dbms_id = data["dbms_id"]

        tipos_dato = TipoDato.query.filter(
           TipoDato.nombre.ilike(tipo_dato_nombre),
           TipoDato.proveedor_bd_id == dbms_id
        ).all()

        return Response(input_data=tipos_dato).get()

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

class Select:
    def __init__(self):
        pass

    def search(self, args):
        tipo_dato_nombre = "%{}%".format(args["tipo_dato_nombre"])
        dbms_id = args["dbms_id"]

        tipos_dato = TipoDato.query.filter(
           TipoDato.nombre.ilike(tipo_dato_nombre),
           TipoDato.proveedor_bd_id == dbms_id
        ).all()

        return Response(input_data=tipos_dato, formatter=SelectFormatter()).get()

class SelectFormatter:
    def __init__(self):
        pass
    
    def format(self, records):
        formatted_records = []

        for row in records:
            formatted_row = {
                "label":row.nombre,
                "value":row.tipo_dato_id,
                "config":Config(row.config).to_dict()
            }
            formatted_records.append(formatted_row)
        return formatted_records

class Config:
    def __init__(self, data):
        self.data = data
    def to_dict(self):
        parts = self.data.split('\n')
        return self.make_params(parts)

    def make_params(self, parts):
        params = []
        for item in parts:
            params.append(self.to_element(item))
        return params

    def to_element(self, item):
        element = {}
        fields = item.split(',')
        for cell in fields:
            cell_parts = cell.split(':')
            cell_key = cell_parts[0] 
            cell_value = cell_parts[1]
            element = {cell_key, cell_value}
        return element

