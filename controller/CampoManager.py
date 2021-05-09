#models
from model.ModelCampo import ModelCampo
from model.Objeto import Objeto
from model.ObjetoProps import ObjetoProps
from model.ProveedorBD import ProveedorBD
from model.TipoDato import TipoDato

#helpers
from helper.Response import JsonResponse, Response
from helper.Transformer import Transformer
from helper.StatusMessage import StatusMessage

#aux
import aux.TipoObjeto as TipoObjeto
import aux.EstadoCodigo as EstadoCodigo

#python
from datetime import datetime
from sqlalchemy.orm import aliased
from flask_sqlalchemy import get_debug_queries
from pprint import pprint
from sqlalchemy import and_
import json

#app
from app import db

class CampoManager:
    

    def __init__(self):
        self.model = ModelCampo()
        pass

    def new(self, data={}):
        tabla_id = data["tabla_id"]
        tabla = Objeto.query.filter(
            Objeto.id == tabla_id
        ).one()

        dbms = ProveedorBD.query.filter(
            ProveedorBD.proveedor_bd_id == tabla.dbms_id
        ).one()

        tabla_props = ObjetoProps.query.filter(
            ObjetoProps.objeto_id == tabla_id
        ).all()

        tabla_dict = Transformer(input_data=tabla).model_to_dict()        

        #fetch all
        for item in tabla_props:
            tabla_dict[item.nombre] = item.valor

        #get database
        database = Objeto.query.filter(
            Objeto.id == tabla_dict["database_id"]
        ).first()

        #get schema
        esquema = Objeto.query.filter(
            Objeto.id == tabla.objeto_padre_id
        ).first()

        tabla_fullname = "{}.{}.{}".format(database.nombre, esquema.nombre, tabla.nombre)

        ans = {
            "tabla_id": tabla.id,
            "tabla_nombre":tabla.nombre,
            "tabla_fullname":tabla_fullname,
            "dbms_id":tabla.dbms_id,
            "dbms_nombre":dbms.nombre           
        }   

        return Response(input_data=ans).get()


    def guardar(self, data={}):

        campo_id = data["campo_id"]
        tipo_dato_id = data["tipo_dato_id"]

        campo = None

        if campo_id in [0,""]:
            campo = Objeto(                
                objeto_padre_id=data["tabla_id"],
                nombre=data["nombre"],
                tipo_objeto_id=TipoObjeto.CAMPO,
                dbms_id=data["dbms_id"],                
                desc_abreviada=data["desc_abreviada"],
                desc_completa=data["desc_completa"],
                estado_id = EstadoCodigo.OBJETO_BORRADOR,
                fch_creacion=datetime.now()
            )

            db.session.add(campo)                        
            db.session.flush()     

        else:        
            campo = Objeto.query.filter(
                Objeto.id == campo_id
            ).one()

            campo.nombre = data["nombre"]
            campo.desc_abreviada=data["desc_abreviada"]
            campo.desc_completa=data["desc_completa"]            
            campo.fch_modificacion=datetime.now()
        
        #save props
        column_props = ColumnProps(campo.id)
        column_props.load_data_type(tipo_dato_id)
        status = column_props.save(column_id=campo.id, data=data)
        if status.success == False:
            return status.make_response()
        
        #return messages
        message = "Se ha guardado correctamente el campo con id: {}".format(campo.id)
        extradata  = {
            "campo_id":campo.id
        }

        db.session.commit()

        return Response(msg=message, data=extradata).get()       

    def get_tipo_dato_text(self, data, syntax=""):
        tipo_dato_text_str = ''
        data_dict = json.loads(data)

        # Los datos se encuentran en el campo tipo_dato
        # _data almacenado json
        for key, value in data_dict.items():
            if len(tipo_dato_text_str) == 0:
                tipo_dato_text_str = syntax

            param='%'+key
            tipo_dato_text_str = tipo_dato_text_str.replace(param, value)

        # Si los datos de precision no se encuentran en bd el texto sera el mismo que el de sintaxis
        if tipo_dato_text_str == "":
            tipo_dato_text_str = syntax

        return tipo_dato_text_str


    def get_campos_por_tabla(self, args={}):
        campo = aliased(Objeto, name="campo")

        result_set = db.session.query(
            campo.id,
            campo.nombre,
            campo.dbms_id,
            campo.desc_abreviada,
            campo.desc_completa,
            campo.estado_id,
            campo.fch_creacion,
            campo.fch_modificacion,
            campo.objeto_padre_id.label("tabla_id"),   
            TipoDato.nombre.label("tipo_dato_nombre")         
        ).outerjoin(ObjetoProps, campo.id == ObjetoProps.objeto_id).\
        outerjoin(TipoDato, ObjetoProps.valor == TipoDato.tipo_dato_id).\
        filter(                        
            campo.objeto_padre_id == args["tabla_id"],
            ObjetoProps.nombre == "tipo_dato_id"
        ).all()

        props = db.session.query(
            ObjetoProps.id,
            ObjetoProps.objeto_id.label('campo_id'),
            ObjetoProps.nombre,
            ObjetoProps.valor
        ).filter(
            ObjetoProps.objeto_id == Objeto.id,
            Objeto.objeto_padre_id == args["tabla_id"]
        ).all()

        return Response(input_data=result_set,formatter=CampoListaFormatter(props=props)).get()

    def get(self, data={}):      
        campo = aliased(Objeto, name="campo")
        tabla = aliased(Objeto, name="tabla")
        dbms = aliased(ProveedorBD, name="dbms")        

        result_set = db.session.query(
            campo.id,
            campo.nombre,
            campo.dbms_id,
            dbms.nombre.label("dbms_nombre"),
            campo.desc_abreviada,
            campo.desc_completa,
            campo.estado_id,
            campo.fch_creacion,
            campo.fch_modificacion,
            campo.objeto_padre_id.label("tabla_id"),
            tabla.nombre.label("tabla_nombre")            
        ).filter(
            campo.objeto_padre_id == tabla.id,
            campo.dbms_id == dbms.proveedor_bd_id,
            campo.id == data["campo_id"]
        ).one()

        #get the props
        props = ColumnProps(data["campo_id"]).get_props(_asdict=True)

        #get the data type and data
        tipo_dato = self._get_tipo_dato(props)        
             
        #pprint(tipo_dato)        
        response = Response(input_data=result_set)
        response.add_extradata("tipo_dato",tipo_dato)
        response.add_extradata("props",props)
        return response.get()

    def _get_tipo_dato(self, props):
        tipo_dato_dict = {}

        tipo_dato = TipoDato.query.filter(
            TipoDato.tipo_dato_id == props["tipo_dato_id"]["valor"]
        ).first()

        if tipo_dato is not None:            
            tipo_dato_dict = Transformer(tipo_dato).model_to_dict()   
            config = json.loads(tipo_dato.config)
            config_with_values = self._get_tipo_dato_vars_value(config, props["tipo_dato_vars"])
            tipo_dato_dict["config"] = config_with_values

        return tipo_dato_dict

    def _get_tipo_dato_vars_value(self, config={}, tipo_dato_vars={}):
        data_vars = json.loads(tipo_dato_vars["valor"])
        for key, value in config.items():
            config[key]["value"] = data_vars[key]

        return config


class CampoListaFormatter:
    def __init__(self, props = []):        
        self.props = props
        self.grouped = {}

    def format(self, records):
        #prepare groups
        self._group_props()

        #eval row by row
        formatted_records = []

        for row in records:
            row_dict = dict(row)            
            row_dict["props"] = self._get_props(row_dict["id"])
            formatted_records.append(row_dict)
    
        return formatted_records


    def _get_props(self, campo_id=None):
        if campo_id in self.grouped:
            return self.grouped[campo_id]
        else:
            return {}

    def _group_props(self):        
        
        for item in self.props:
            valor = None
            if item.nombre == "tipo_dato_vars":
                valor = json.loads(item.valor)
            else:
                valor = item.valor

            if item.campo_id not in self.grouped:
                self.grouped[item.campo_id] = {
                    item.nombre:valor
                }
            else:
                self.grouped[item.campo_id][item.nombre] = valor

class ColumnProps:
    def __init__(self, column_id=None):
        self.status = StatusMessage()   
        self.column_id = column_id                
        self.props = []
        self.tipo_dato = None

    def load_data_type(self, tipo_dato_id):
        self.tipo_dato = TipoDato.query.filter(TipoDato.tipo_dato_id == tipo_dato_id).first()                    

    def _add_prop(self, key, value):
        self.props.append(
                {"nombre":key,"valor":value, "objeto_id":self.column_id}
            )

    def _add_tipo_dato_vars(self, params={}):
        tipo_dato_vars = {
            "nombre":"tipo_dato_vars",
            "flg_activo":"S",
            "valor":{}
        }

        prop_valor = {}

        for var, item in params.items():
            prop_valor[var] = item["value"]
        
        tipo_dato_vars["valor"] = json.dumps(prop_valor)
        self.props.append(tipo_dato_vars)
        return tipo_dato_vars

    def _add_tipo_dato_pattern(self):        
        prop = {
            "nombre":"tipo_dato_pattern",
            "flg_activo":"S",
            "valor":self.tipo_dato.nombre
        }

        self.props.append(prop)
        return prop

    def _add_tipo_dato_def(self, tipo_dato_vars = None, tipo_dato_syntax=""):
        tipo_dato_def = ""
        if tipo_dato_vars is not None:
            vars_as_dict = json.loads(tipo_dato_vars["valor"])

            for key, value in vars_as_dict.items():

                var_to_replace = "%"+key
                tipo_dato_def = tipo_dato_syntax.replace(var_to_replace, value)        

        prop = {
            "nombre":"tipo_dato_def",
            "flg_activo":"S",
            "valor":tipo_dato_def
        }
        self.props.append(prop)

    def save(self, column_id=None, data={}):
        self.save_validation(data)
        if self.status.success == False:
            return self.status

        #begin process
        self._add_prop("flg_pk",data["flg_pk"])
        self._add_prop("flg_mandatory",data["flg_mandatory"])
        self._add_prop("tipo_dato_id",data["tipo_dato_id"])
        self._add_prop("project_id",data["project_id"])
        prop_tipo_dato_vars = self._add_tipo_dato_vars(data["tipo_dato_params"])
        prop_tipo_dato_syntax = self._add_tipo_dato_pattern()
        self._add_tipo_dato_def(prop_tipo_dato_vars, prop_tipo_dato_syntax["valor"])

        #processing props
        for item in self.props:
            prop = ObjetoProps.query.filter(
                ObjetoProps.nombre == item["nombre"],
                ObjetoProps.objeto_id == self.column_id
            ).first()

            if prop is not None:
                prop.valor = item["valor"]
            else:
                prop = ObjetoProps(
                    nombre = item["nombre"],
                    objeto_id = self.column_id,
                    valor = item["valor"],
                    flg_activo="S",
                    fch_creacion=datetime.now()
                )

                db.session.add(prop)

        return self.status

    def save_validation(self, data={}):
        if "flg_pk" not in data:
            return self.status.error("flg_pk no enviado")
        if "flg_mandatory" not in data:
            return self.status.error("flg_mandatory no enviado")
        if "tipo_dato_id" not in data:
            return self.status.error("tipo_dato_id no enviado")
        if "project_id" not in data:
            return self.status.error("project_id no enviado")
        if "tipo_dato_params" not in data:
            return self.status.error("tipo_dato_params no enviado")
        return self.status

    def get_props(self, _asdict=False):
        result = {}

        rows = ObjetoProps.query.filter(
            ObjetoProps.objeto_id == self.column_id            
        ).all()

        for objeto_prop in rows:
            if _asdict == True:
                result[objeto_prop.nombre] = Transformer(objeto_prop).model_to_dict()                
            else:
                result[objeto_prop.nombre] = objeto_prop

        return result

    def _get_props(self):
        result = {}

        rows = ObjetoProps.query.filter(
            ObjetoProps.objeto_id == self.column_id            
        ).all()

        for objeto_prop in rows:
            if objeto_prop.nombre == "tipo_dato_pattern":
                result[objeto_prop.nombre] = dict(objeto_prop.valor)
            else:
                result[objeto_prop.nombre] = objeto_prop.valor

        return result


