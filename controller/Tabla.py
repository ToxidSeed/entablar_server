#helpers
from helper.Transformer import Transformer
from helper.Response import Response, JsonResponse
from helper.StatusMessage import StatusMessage
import helper.Database as hdb

#models
from model.Objeto import Objeto
from model.ObjetoProps import ObjetoProps
from model.ProyectoObjeto import ProyectoObjeto

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

    def new(self, data={}):
        input_data = {
            "estado_nombre":"Borrador"
        }
        return Response(input_data=input_data).get()

    def guardar(self, data={}):
        #validation
        status = self.guardar_validation(data)
        if status.success == False:
            return status.make_response()

        #start processing
        tabla_id = data["tabla_id"]        

        if tabla_id in [0,""]:
            tabla = self._save_new(data)
            tabla_id = tabla.id            
        else:
            tabla = self._save_existing(data, tabla_id)

        status = TablaProps().save(tabla_id, data)
        if status.success == False:
            return status.make_response()
        
        message = "Se ha guardado correctamente la tabla con id: {}".format(tabla.id)
        db.session.commit()

        response = Response(msg=message)
        response.add_extradata("object",{
            "tabla_id":tabla.id,
            "fch_creacion":tabla.fch_creacion
        })
        return response.get()


    def guardar_validation(self, args=None):
        status = StatusMessage()

        if args is None:
            return status.error(message="args is None")

        if "project_id" not in args:
            return status.error(message="No se ha enviado el parámetro project_id")
        
        if args["project_id"] in ["",0]:
            return status.error(message="El valor {} de project_id es invalida".format(args["proyecto_id"]))

        return status

        #return self.answer.__dict__

    def _save_new(self, data={}):
        tabla = Objeto(
            nombre=data["nombre"], 
            tipo_objeto_id=self.TIPO_OBJETO_TABLA,
            dbms_id=data["dbms_id"],            
            objeto_padre_id=data["esquema_id"],
            desc_abreviada=data["desc_abreviada"],
            desc_completa=data["desc_completa"],
            fch_modificacion=datetime.now()
        )

        tabla.estado_id = self.ESTADO_TABLA_ELIMINADO
        tabla.fch_creacion=datetime.now()
        db.session.add(tabla)                        
        db.session.flush()
        return tabla

    def _save_existing(self, data={}, tabla_id=None):        
        tabla = Objeto.query.filter_by(id=tabla_id).first()
        tabla.nombre = data["nombre"]
        tabla.objeto_padre_id=data["esquema_id"]
        tabla.desc_abreviada = data["desc_abreviada"]
        tabla.desc_completa = data["desc_completa"]
        tabla.fch_modificacion = datetime.now()
        return tabla

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
            if element.nombre == "database_id":
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

class TablaProps:
    def __init__(self):
        self.props = []

    def save(self, tabla_id=None, args={}):
        status = StatusMessage()
        if "database_id" not in args:
            return status.error("database_id no ha sido enviado")
        if "project_id" not in args:
            return status.error("project_id no ha sido enviado")

        self.add_database(tabla_id, args["database_id"])
        self.add_project(tabla_id, args["project_id"])

        #save
        for object_prop in self.props:
            object_prop.fch_creacion = datetime.now()
            object_prop.fch_modificacion = datetime.now()
            object_prop.flg_activo = "S"
            db.session.add(object_prop)

        return status

    def add_database(self, tabla_id, database_id):
        database_prop = ObjetoProps(objeto_id=tabla_id, nombre="database_id", valor=database_id)
        self.props.append(database_prop)

    def add_project(self, tabla_id, project_id):
        project_prop = ObjetoProps(objeto_id=tabla_id, nombre="project_id", valor=project_id)
        self.props.append(project_prop)

class TablaScriptCreator:
    def __init__(self):
        pass

    def create(self, args={}):
        tabla_id = args["tabla_id"]

        table = Objeto.query.filter(
            Objeto.id == tabla_id
        ).one()

        columns = Objeto.query.filter(
            Objeto.objeto_padre_id == tabla_id
        ).all()

        col_template = self.get_col_template()
        cols_list = []
        for col in columns:
            props = self.get_props(col.id)
            col_definition = col_template.format(column_name=col.nombre, data_type=props["tipo_dato_def"])
            cols_list.append(col_definition)
                
        columns_definition_str = ",".join(cols_list)

        #make table
        tab_template = self.get_table_template()
        tab_definition = tab_template.format(table_name=table.nombre, columns=columns_definition_str)
        print(tab_definition)
        return Response(data=tab_definition).get()

    def get_table_template(self):
        return  "CREATE TABLE {table_name}({columns})"
    
    def get_col_template(self):
        return  '{column_name} <span style="color:blue;">{data_type}</span>'

    def get_props(self, col_id):
        object_props = ObjetoProps.query.filter(
            ObjetoProps.objeto_id == col_id
        ).all()

        col_props = {}
        for prop in object_props:
            col_props[prop.nombre] = prop.valor

        return col_props






