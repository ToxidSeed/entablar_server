from model.ModelTabla import ModelTabla
from domain.DomainTabla import DomainTabla
from controller.Campo import Campo
from controller.ProveedorBD import ProveedorBD
from export.script.oracle.TableCreator import TableCreator
from helper.Response import Response


class Tabla:
    ESTADO_TABLA_ELIMINADO = 0
    DEFAULT_ID = -1

    def __init__(self):
        self.model = ModelTabla()
        self.answer = None
        pass

    def guardar(self, data={}):
        obj = DomainTabla()
        obj.nombre = data["nombre"]
        obj.descripcion = data["descripcion"]
        obj.dbms_id = data["dbms_id"]

        # Si no se envía el dato de la tabla
        if data["tabla_id"] in [0, ""]:
            self.model.insertar(obj)
            self.answer = Response("00001", obj.__dict__, (obj.tabla_id, obj.nombre))
        else:
            obj.tabla_id = data["tabla_id"]
            self.model.actualizar(obj)
            self.answer = Response("00001", obj.__dict__)

        return self.answer.__dict__

    def eliminar(self, data={}):
        stmt = self.model.get_query("tabla_eliminar")
        self.model.execute_update(stmt, data)
        self.answer = Response("00003", msg_data=(data["tabla_id"],))
        return self.answer.__dict__

    def recuperar(self, data={}):
        stmt = self.model.get_query("tabla_recuperar")
        self.model.execute_update(stmt, data)
        self.answer = Response("00004", msg_data=(data["tabla_id"],))
        return self.answer.__dict__

    def get_object(self, data={}):
        params = (data["tabla_id"],)
        obj = self.model.get_object(params)
        obj_dict = obj.__dict__

        self.get_dbms(obj_dict)
        self.get_estado(obj_dict)

        return obj_dict

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
        obj_ctrl_dbms = ProveedorBD()
        obj_dbms = obj_ctrl_dbms.get_object({
            'proveedor_bd_id':obj_tabla['dbms_id']
        })
        obj_campo = Campo()
        list_campos_tabla = obj_campo.get_campos_por_tabla(params)

        obj_table_creator = TableCreator()
        obj_table_creator.table_name = obj_tabla['nombre']
        obj_table_creator.fields = list_campos_tabla['rows']
        return obj_table_creator.create_table()


