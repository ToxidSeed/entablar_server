
from helper.Transformer import Transformer
from helper.Response import Response, JsonResponse
import helper.Database as hdb
from model.Objeto import Objeto
from model.ObjetoProps import ObjetoProps
from domain.DomainTabla import DomainTabla
from controller.Campo import Campo
from export.script.oracle.TableCreator import TableCreator
from app import db
from sqlalchemy import func
from datetime import datetime
from model.Estado import Estado

from aux.EstadoObjeto import EstadoObjeto
import aux.TipoObjeto as TipoObjeto
import aux.EstadoCodigo as EstadoCodigo

from sqlalchemy import and_, text


class Tabla:
    ESTADO_TABLA_ELIMINADO = 0
    ESTADO_TABLA_REGISTRADO =1    
    TIPO_OBJETO_TABLA = 2

    def __init__(self):
        self.model = None
        self.answer = None
        pass

    def guardar(self, data={}):
        tabla_id = data["tabla_id"]

        tabla = Objeto(
            nombre=data["nombre"], 
            tipo_objeto_id=self.TIPO_OBJETO_TABLA,
            dbms_id=data["dbms_id"],            
            objeto_padre_id=data["esquema_id"],
            desc_abreviada=data["desc_abreviada"],
            desc_completa=data["dçesc_completa"],
            fch_modificacion=datetime.now()
        )

        if tabla_id in [0,""]:
            tabla.estado_id = self.ESTADO_TABLA_ELIMINADO
            tabla.fch_creacion=datetime.now()
            db.session.add(tabla)                        
            db.session.flush()

            #database_id
            #esquema_id
            database_id_prop = ObjetoProps(objeto_id = tabla.id,nombre = "DATABASE_ID",valor=data["database_id"], fch_creacion =datetime.now(), fch_modificacion=datetime.now()) 
            db.session.add(database_id_prop)            
        else:
            tabla_to_update = Objeto.query.filter_by(id=tabla_id).first()

        message = "Se ha guardado correctamente la tabla con id: {}".format(tabla.id)
        extradata  = {
            "tabla_id":tabla.id,
            "fch_creacion":tabla.fch_creacion
        }

        db.session.commit()
        
        return Response(msg=message, extradata=extradata).get()

        #return self.answer.__dict__

    def eliminar(self, data={}):
        ids_eliminar = data['ids_eliminar']

        for identifier in ids_eliminar:                      
            db.session.query(Objeto).filter_by(id = identifier).update({"estado_id": EstadoCodigo.OBJETO_ELIMINADO})
            db.session.flush()

        db.session.commit()
        

    def recuperar(self, data={}):
        stmt = self.model.get_query("tabla_recuperar")
        self.model.execute_update(stmt, data)
        self.answer = Response("00004", msg_data=(data["tabla_id"],))
        return self.answer.__dict__

    def get(self, args={}):

        tabla_id = args["tabla_id"]
        tabla = Objeto.query.filter(        
            Objeto.id == tabla_id
        ).one()

        tabla_dict = Transformer(tabla).model_to_dict()

        #otros datos de la tabla
        tabla_props = ObjetoProps.query.filter(
            ObjetoProps.objeto_id == tabla_id
        ).all()

        for element in tabla_props:
            if element.nombre == "DATABASE_ID":
                tabla_dict["database_id"] = element.valor

        #estado de la tabla
        estado = EstadoObjeto().get(tabla.estado_id)
        tabla_dict["estado_nombre"] = estado.nombre

        return Response(input_data=tabla_dict).get()    

    def get_dbms(self, tabla_dict=None):
        tabla_dict["dbms_nombre"] = ""

        if 'dbms_id' in tabla_dict:
            if tabla_dict["dbms_id"] is not None:
                dbms_obj = self.model.get_single_result(
                    script_name = 'proveedor_bd_get',
                    params = (tabla_dict["dbms_id"],)
                )
                if dbms_obj is not None:
                    tabla_dict["dbms_nombre"] = dbms_obj["nombre"]

    def get_estado(self, tabla_dict=None):
        tabla_dict["estado_tabla_nombre"] = ""

        if 'estado_tabla_id' in tabla_dict:
            if tabla_dict["estado_tabla_id"] is not None:
                estado_tabla_obj = self.model.get_single_result(
                    script_name = 'estado_tabla_get',                    
                    params = tabla_dict
                )
                if estado_tabla_obj is not None:
                    tabla_dict["estado_tabla_nombre"] = estado_tabla_obj["nombre"]

    def get_tablas_list(self, data={}):
        query_str = self.model.get_query("tabla_get_tablas_list")
        estado_tabla_id = self.DEFAULT_ID
        if data["mostrar_tablas_eliminadas"] == 1:
            estado_tabla_id = self.ESTADO_TABLA_ELIMINADO

        params = {
            "nombre": '%'+data["nombre"]+'%',
            "estado_tabla_id": estado_tabla_id
        }

        result_set = self.model.execute_query(query_str, params)
        response = {
            "rows": result_set
        }
        return response

    def exportar(self, params={}):  
        obj_tabla = self.get_object(params)
        obj_campo = Campo()
        list_campos_tabla = obj_campo.get_campos_por_tabla(params)

        obj_table_creator = TableCreator()
        obj_table_creator.table_name = obj_tabla['nombre']
        obj_table_creator.fields = list_campos_tabla['rows']
        return obj_table_creator.create_table()

class TablaList:
    def __init__(self):
        pass

    def get(self, args={}):        
        sql = text(hdb._get_query('tabla_list').format(**args)) 
        results_set = db.engine.execute(sql)        
        return Response(input_data=results_set).get()
