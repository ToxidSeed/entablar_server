from model.ModelCampo import ModelCampo
from model.Objeto import Objeto
from model.ObjetoProps import ObjetoProps
from model.ProveedorBD import ProveedorBD
from model.TipoDato import TipoDato

from domain.DomainCampo import DomainCampo
from sqlalchemy import and_
import json
from helper.Response import JsonResponse, Response
from helper.Transformer import Transformer

#aux
import aux.TipoObjeto as TipoObjeto
import aux.EstadoCodigo as EstadoCodigo

#python
from datetime import datetime

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
            Objeto.id == tabla_dict["DATABASE_ID"]
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
        """obj = DomainCampo()
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
        return obj.__dict__"""

        campo_id = data["campo_id"]

        campo = None

        if campo_id in [0,""]:
            campo = Objeto(                
                objeto_padre_id=data["tabla_id"],
                nombre=data["nombre"],
                tipo_objeto_id=TipoObjeto.CAMPO,
                dbms_id=data["dbms_id"],                
                desc_abreviada="",
                desc_completa=data["desc_completa"],
                estado_id = EstadoCodigo.OBJETO_BORRADOR,
                fch_creacion=datetime.now()
            )

            db.session.add(campo)                        
            db.session.flush()     

        else:        
            campo = Objeto.query.filter(
                Objeto.id == campo_id
            )

            campo.desc_completa=data["desc_completa"]
            campo.fch_modificacion=datetime.now()

        #save props
        ColumnProps(data, campo.id).save()

        message = "Se ha guardado correctamente el campo con id: {}".format(campo.id)
        extradata  = {
            "campo_id":campo.id
        }

        db.session.commit()

        return Response(msg=message, data=extradata).get()

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


    def get_campos_por_tabla(self, args={}):
        """campos_found = Objeto.query.filter(
            and_(
                Objeto.tipo_objeto_id == self.TIPO_OBJETO_CAMPO,
                Objeto.objeto_padre_id == args["tabla_id"]
            )
        ).all()
        
        return Response(input_data=campos_found).get()"""

    def get(self, data={}):
        """params = (data["campo_id"],)
        query_str = self.model.get_query("campo_get")
        obj = self.model.get_single_result(query_str, params)
        return obj"""

        campo = Objeto.query.filter(
            Objeto.id == data["campo_id"]
        ).one()

        """campo_dict = Transformer(campo).model_to_dict()

        campo_props = ObjetoProps.query.filter(
            ObjetoProps.objeto_id == data["campo_id"]
        ).all()

        campo_dict["props"]={}
        for prop in campo_props:
            campo_dict["props"][prop.nombre] = Transformer(prop).model_to_dict()

        return Response(input_data=campo_dict).get()"""



class ColumnProps:
    def __init__(self, data, column_id):
        self.data = data
        self.column_id = column_id
        self.props = [
            {"nombre":"TIPO_DATO_ID","valor":data["tipo_dato_id"], "objeto_id":column_id}
        ]

        for param in data["tipo_dato_params"]:
            self.props.append(
                {"nombre":param["var"],"valor":param["valor"], "objeto_id":column_id}
            )

    def save(self):                
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
    
    

