from model.Proyecto import Proyecto
from model.ProyectoUsuario import ProyectoUsuario
from model.Usuario import Usuario
from model.ObjetoProps import ObjetoProps
from model.Objeto import Objeto
from model.TipoObjeto import TipoObjeto

#helper
from helper.Response import Response
from helper.Transformer import Transformer

#application
from app import db
from sqlalchemy import or_, and_

class ProyectoManager:
    def __init__(self):
        pass

    def save(self, data={}):
        proyecto_id = data["id"]

        if proyecto_id in ["",0]:
            self.save_new(data)
        else:
            self.update_existing(data)
        db.session.commit()
    
    def save_new(self, data={}):
        proyecto = Proyecto(
            nombre=data["nombre"],
            descripcion=data["descripcion"]
        )

        db.session.add(proyecto)


    def update_existing(self, data={}):
        proyecto = Proyecto.query.filter(
            Proyecto.id == data["id"]
        ).one()

        proyecto.nombre = data["nombre"]
        proyecto.descripcion = data["descripcion"]

    def search(self, data={}):
        search_text = "%{}%".format(data["search_text"])

        results = Proyecto.query.filter(
            or_(Proyecto.nombre.ilike(search_text), Proyecto.descripcion.ilike(search_text))
        ).all()

        print(Proyecto.query)

        return Response(input_data=results).get()

    def get(self, args={}):
        proyecto_id = args['proyecto_id']

        proyecto = Proyecto.query.filter(
            Proyecto.id == proyecto_id
        ).one()

        return Response(input_data=proyecto).get()

    def get_users(self, args={}):
        proyecto_id = args['proyecto_id']

        users = db.session.query(
            ProyectoUsuario.id,
            ProyectoUsuario.proyecto_id,
            ProyectoUsuario.usuario_id,
            Usuario.nombre,
            Usuario.email
        ).join(Usuario, ProyectoUsuario.usuario_id == Usuario.id).\
        filter(ProyectoUsuario.proyecto_id == proyecto_id).\
        all()

        return Response(input_data=users).get()

    def get_objects(self, args={}):
        proyecto_id = args["proyecto_id"]

        objetos = db.session.query(
            ObjetoProps.objeto_id,
            Objeto.nombre,
            Objeto.tipo_objeto_id,
            TipoObjeto.nombre.label("tipo_objeto_nombre")
        ).join(Objeto, ObjetoProps.objeto_id == Objeto.id)\
        .join(TipoObjeto, Objeto.tipo_objeto_id == TipoObjeto.id)\
        .filter(
            and_(
                ObjetoProps.nombre == "project_id",
                ObjetoProps.valor == proyecto_id 
            )
        ).all()
        #.join(TipoObjeto, Objeto.tipo_objeto_id == TipoObjeto.id)\

        return Response(input_data=objetos).get()

    def add_user(self, args={}):        
        new_project_user = ProyectoUsuario(
            proyecto_id = args["proyecto_id"],
            usuario_id = args["user_id"]
        )

        db.session.add(new_project_user)
        db.session.commit()

    def remove_user(self, args={}):
        relation = ProyectoUsuario.query.filter(
            ProyectoUsuario.id == args["relation_id"]
        ).one()

        db.session.delete(relation)
        db.session.commit()







        
