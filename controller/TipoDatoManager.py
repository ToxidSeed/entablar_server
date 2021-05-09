#from model.ModelTipoDato import ModelTipoDato
from model.TipoDato import TipoDato
from domain.DomainTipoDato import DomainTipoDato
from model.ProveedorBD import ProveedorBD

from helper.Response import Response
from helper.Transformer import Transformer

#
import os, json, re, ast
from app import db
from pprint import pprint


class TipoDatoManager:

    def __init__(self):
        pass

    def guardar(self, data={}):    

        tipo_dato_id = data["id"]    

        tipo_dato = None
        if tipo_dato_id in ["",0]:
            tipo_dato = TipoDato(
                proveedor_bd_id=data["dbms_id"],
                nombre=data["nombre"],
                descripcion=data["descripcion"],
                #config=data["config"],
                config_raw=data["config_raw"],
                config=json.dumps(self._raw_config_to_dict(data["config_raw"]))
            )            
            db.session.add(tipo_dato)
        else:
            tipo_dato = TipoDato.query.filter(
                TipoDato.tipo_dato_id == tipo_dato_id
            ).one()

            tipo_dato.nombre = data["nombre"]
            tipo_dato.descripcion=data["descripcion"]
            tipo_dato.config_raw=data["config_raw"]
            tipo_dato.config = json.dumps(self._raw_config_to_dict(data["config_raw"]))
        
        db.session.commit()

        msg = "Se ha guardado el tipo de dato con código {}".format(tipo_dato.tipo_dato_id)

        return Response(msg=msg,input_data=tipo_dato).get()

    def _raw_config_to_dict(self, config):
        config_dict = {}
        config_list = self._parse_config(config)
        for item in config_list:
            config_dict[item["var"]] = item
        return config_dict


    def _parse_config(self, config):
        parsed_lines = []

        lines = config.split("\n")
        parsed_lines = self._process_list(lines)        
        
        return parsed_lines

    def _process_list(self,lines):  
        parsed_list =  []      
        for line in lines:
            parts = line.split(",")
            parsed_line = self._process_parts(parts)       
            #add full parsed line
            parsed_list.append(parsed_line)
        return parsed_list

    def _process_parts(self, parts):
        parsed_element = {}
        for item in parts:
            elements = item.split(":")
            key = elements[0]
            value = elements[1]
            parsed_element[key] = value
        return parsed_element

    def _get_tipo_dato_vars(self):
        vars_value = {}
        if "tipo_dato_vars" in self.column_props:
            vars_value = json.loads(self.column_props["tipo_dato_vars"]["valor"]) 
        return vars_value
    
    def _get_prop_val(self, var):
        result = {"valor":""}

        if var in self.tipo_dato_vars:
            result["valor"] = self.tipo_dato_vars[var]
        
        return result
    

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
            config = ""
            if row.config != "":
                config = json.loads(row.config)

            formatted_row = {
                "label":row.nombre,
                "value":row.tipo_dato_id,
                "config":config
            }
            formatted_records.append(formatted_row)              
        return formatted_records

class Config:
    def __init__(self, data):
        self.data = data.strip()
    def to_dict(self):
        if self.data == "":
            return []

        parts = self.data.split('\n')        
        return self.make_params(parts)

    def make_params(self, parts):
        params = []
        for item in parts:
            element = self.to_element(item)
            if element is not None:
                params.append(element)
        return params

    def to_element(self, item):
        element = {}

        if item == "":
            return None
        
        fields = item.split(',')

        for cell in fields:
            cell_parts = cell.split(':')

            cell_key = cell_parts[0] 
            cell_value = cell_parts[1]
            element[cell_key] = cell_value

        return element

