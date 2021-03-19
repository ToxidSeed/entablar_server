from controller.ObjetoController import ObjetoController
from model.Objeto import Objeto
from sqlalchemy import and_
from helper.Response import JsonResponse, Response
from datetime import datetime
from app import db

class EsquemaController(ObjetoController):
    def __init__(self):
        ObjetoController.__init__(self,self.TIPO_ESQUEMA)

    def guardar(self, data={}):
        esquema_id = data["esquema_id"]

        esquema = Objeto(
            nombre=data["nombre"], 
            tipo_objeto_id=self._tipo_objeto_id,
            objeto_padre_id=data["database_id"],
            dbms_id=data["dbms_id"],                     
            fch_modificacion=datetime.now()
        )

        if esquema_id in [0, ""]:
            esquema.estado_id = self._tipo_objeto_id
            esquema.fch_creacion = datetime.now()
            db.session.add(esquema)
            db.session.flush()
        else:
            db.session.query(esquema).update({"id",esquema_id})

        message = "Se ha guardado correctamente el esquema con id: {}".format(esquema.id)
        extradata = {
            "esquema_id":esquema.id,
            "fch_creacion":esquema.fch_creacion
        }

        db.session.commit()
        return Response(msg=message, data=extradata).get()

    def get(self, args={}):
        esquema = Objeto.query.filter(
            Objeto.id == args["esquema_id"]
        ).one()

        return Response(input_data=esquema).get()


class AutoComplete(ObjetoController):
    def __init__(self):
        ObjetoController.__init__(self, self.TIPO_ESQUEMA)

    def search(self, args):
        search_text = "%{}%".format(args["nombre"])
        database_id = args["database_id"]

        if(database_id == ""):            
            objects_found = Objeto.query.filter(
                and_(Objeto.nombre.ilike(search_text),
                Objeto.tipo_objeto_id == self._tipo_objeto_id
                )                
            ).all()
        else:
            objects_found = Objeto.query.filter(
                and_(
                    Objeto.nombre.ilike(search_text),
                    Objeto.tipo_objeto_id == self._tipo_objeto_id,
                    Objeto.objeto_padre_id == database_id
                )
            ).all()

        return JsonResponse(objects_found, formatter=AutocompleteFormatter()).make() 

class AutocompleteFormatter:
    def __init__(self):
        pass

    def format(self, records):
        formatted_records = []

        for row in records:
            formatted_row = {
                "label":row["nombre"],
                "value":row["id"],
                "dbms_id":row["dbms_id"],
                "database_id":row["objeto_padre_id"]
            }

            formatted_records.append(formatted_row)

        return formatted_records
