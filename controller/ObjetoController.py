import helper.Database as hdb
from model.Objeto import Objeto
from helper.Response import JsonResponse

class ObjetoController:
    TIPO_BASE_DATOS = 1
    TIPO_TABLA = 2
    TIPO_CAMPO = 3
    TIPO_ESQUEMA = 4

    def __init__(self, tipo_objeto_id):
        self._tipo_objeto_id = tipo_objeto_id

    def search(self, args):
        """args["search_text"] = '%'+args["search_text"]+'%'
        response = hdb.execute_query("objeto_search", args, show_last_executed=True)
        json_response = JsonResponse(response)
        return json_response.make()"""

        search_text = "%{}%".format(args["search_text"])
        objects_found = Objeto.query.filter(
            Objeto.nombre.ilike(search_text), 
            Objeto.desc_abreviada.ilike(search_text), 
            Objeto.desc_completa.ilike(search_text)
        ).all()

        return JsonResponse(objects_found).make()

        

