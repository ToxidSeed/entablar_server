from model.ModelProveedorBD import ModelProveedorBD
from model.ProveedorBD import ProveedorBD
from helper.Response import JsonResponse, Response
from domain.DomainProveedorBD import DomainProveedorBD
import os


class ProveedorBDController:

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

    def get(self, args={}):
        proveedor_bd = ProveedorBD.query.filter(
            ProveedorBD.proveedor_bd_id == args["proveedor_bd_id"]
        ).one()

        return Response(input_data=proveedor_bd).get()

    def get_list(self, args={}):
        """nombre = "%{}%".format(args["nombre"])
        proveedores_found = ProveedorBD.query.filter(ProveedorBD.nombre.ilike(nombre)).all() 
        return JsonResponse(proveedores_found).make()
        """

        search_text = "%{}%".format(args["nombre"])        
        proveedores_found = ProveedorBD.query.filter(ProveedorBD.nombre.ilike(search_text)).all()
        return Response(input_data=proveedores_found).get()


class AutoComplete:
    def __init__(self):
        pass

    def search(self, args):
        search_text = "%{}%".format(args["nombre"])
        
        proveedores_found = ProveedorBD.query.filter(ProveedorBD.nombre.ilike(search_text)).all()        
        return JsonResponse(proveedores_found, formatter=AutoCompleteFormatter()).make()

class AutoCompleteFormatter:
    def __init__(self):
        pass

    def format(self, records):
        formatted_records = []
        #Rename
        for row in records:
            formatted_row = {
                "label":row["nombre"],
                "value":row["proveedor_bd_id"]
            } 
            formatted_records.append(formatted_row)

        #print(formatted_records)
        return formatted_records
