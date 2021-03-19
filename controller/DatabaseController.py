from model.Objeto import Objeto
from helper.Response import JsonResponse, Response
from sqlalchemy import and_
from datetime import datetime
from app import db

class DatabaseController:
    TIPO_OBJETO_ID = 1
    ESTADO_TABLA_BORRADOR_ID = 0
    def __init__(self):
        pass

    def guardar(self, data={}):
        database_id = data["database_id"]

        database = Objeto(
            nombre=data["nombre"], 
            tipo_objeto_id=self.TIPO_OBJETO_ID,
            dbms_id=data["dbms_id"],                     
            fch_modificacion=datetime.now()
        )

        if database_id in [0,""]:
            database.estado_id = self.ESTADO_TABLA_BORRADOR_ID
            database.fch_creacion = datetime.now()
            db.session.add(database)                        
            db.session.flush()
        else:
            db.session.query(database).update({"id": database_id})

        message = "Se ha guardado correctamente la base de datos con id: {}".format(database.id)
        extradata  = {
            "database_id":database.id,
            "fch_creacion":database.fch_creacion
        }

        db.session.commit()
        
        return Response(msg=message, data=extradata).get()

    def get(self, args={}):
        database = Objeto.query.filter(
            Objeto.id == args["database_id"]
        ).one()

        return Response(input_data=database).get()

class AutoComplete:
    TIPO_OBJETO_ID_BASE_DATOS = 1
    def __init__(self):
        pass

    def search(self, args):
        search_text = "%{}%".format(args["nombre"])
        dbms_id = args["dbms_id"]

        if (dbms_id == ""):
            databases_found = Objeto.query.filter(
                and_(Objeto.nombre.ilike(search_text), 
                Objeto.tipo_objeto_id == self.TIPO_OBJETO_ID_BASE_DATOS)
            ).all()
        else:
            databases_found = Objeto.query.filter(
                and_(Objeto.nombre.ilike(search_text), 
                Objeto.tipo_objeto_id == self.TIPO_OBJETO_ID_BASE_DATOS,
                Objeto.dbms_id == dbms_id)
            ).all()

        return JsonResponse(databases_found, formatter=AutoCompleteFormatter()).make()

class AutoCompleteFormatter:
    def __init__(self):
        pass

    def format(self, records):
        formatted_records = []

        for row in records:
            formatted_row = {
                "label":row["nombre"],
                "value":row["id"],
                "dbms_id":row["dbms_id"]
            }
             
            formatted_records.append(formatted_row)
        
        return formatted_records
