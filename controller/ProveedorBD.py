from model.ModelProveedorBD import ModelProveedorBD
from domain.DomainProveedorBD import DomainProveedorBD
import os


class ProveedorBD:

    def __init__(self):
        self.model = ModelProveedorBD()
        self.upload_folder = './upload/images/'

    def guardar(self, data={}):
        file = data['files']['file']
        filename_up = file.filename
        obj = DomainProveedorBD()
        obj.nombre = data['form']['nombre']
        obj.icono = filename_up
        self.model.insertar(obj)
        filename = str(obj.proveedor_bd_id) + "_" + filename_up
        file.save(os.path.join(self.upload_folder, filename))
        return obj.__dict__

    def get_object(self, data={}):
        params = (data["proveedor_bd_id"],)
        query_str = self.model.get_query("proveedor_bd_get")
        result_set = self.model.execute_query(query_str, params)
        response = {}
        if len(result_set) == 1:
            response = result_set[0]

        return response

    def get_list(self, data={}):
        query_str = self.model.get_query("proveedor_bd_get_list")
        params = ('%'+data["nombre"]+'%',)
        result_set = self.model.execute_query(query_str, params)
        response = {
            "rows": result_set
        }
        return response


