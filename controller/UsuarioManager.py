import traceback

from domain.DomainUsuario import DomainUsuario
from helper.Response import Response
from model.ModelUsuario import ModelUsuario
from model.Usuario import Usuario
from model.ProyectoUsuario import ProyectoUsuario
from model.Proyecto import Proyecto
from sqlalchemy import or_

#app
from app import db


class UsuarioManager:
    def __init__(self):
        self.response = Response()
        self.model = ModelUsuario(self.response)

    def registrar(self, data={}):
        try:
            self.validate_register_input_data(data)
            if not self.response.exist_error():
                usuario_id = self.model.registrar(data)
                if usuario_id is None:
                    self.response.set_failure_msg("usuario_failure_register")
                else:
                    self.response.set_success_msg("usuario_success_register", (usuario_id, ))

            return self.response.get()
        except:
            return traceback.format_exc()

    def validate_register_input_data(self, data={}):
        if "nombre_usuario" not in data.keys():
            self.response.add_error_msg("usuario_register_usuario_id_required")
        if "nombres" not in data.keys():
            self.response.add_error_msg("usuario_register_nombres_required")
        if "apellidos" not in data.keys():
            self.response.add_error_msg("usuario_register_apellidos_required")
        if "password" not in data.keys():
            self.response.add_error_msg("usuario_register_password_required")
        if "rePassword" not in data.keys():
            self.response.add_error_msg("usuario_register_retype_pass_required")
        if "nombre_usuario" in data.keys() and len(data["nombre_usuario"]) == 0:
            self.response.add_error_msg("usuario_register_nombre_usuario_zero_len")
        if "nombres" in data.keys() and len(data["nombres"]) == 0:
            self.response.add_error_msg("usuario_register_nombres_zero_len")
        if "apellidos" in data.keys() and len(data["apellidos"]) == 0:
            self.response.add_error_msg("usuario_register_apellidos_zero_len")
        if "password" not in data.keys():
            self.response.add_error_msg("usuario_register_password_zero_len")
        if "rePassword" not in data.keys():
            self.response.add_error_msg("usuario_register_retype_pass_zero_len")

    def get_projects(self, args={}):
        proyectos = db.session.query(
            ProyectoUsuario.proyecto_id,
            ProyectoUsuario.usuario_id,
            Proyecto.nombre
        ).join(Proyecto, Proyecto.id == ProyectoUsuario.proyecto_id)\
        .filter(
            ProyectoUsuario.usuario_id == args["usuario_id"]
        ).all()

        return Response(input_data=proyectos).get()


class AutoComplete:
    def __init__(self):
        pass

    def search(self, args={}):
        search_text = "%{}%".format(args["search_text"])

        usuarios = db.session.query(
            Usuario.id,
            Usuario.nombre,
            Usuario.email
        ).filter(
            or_(Usuario.nombre.ilike(search_text), Usuario.email.ilike(search_text))
        ).all()

        return Response(input_data=usuarios, formatter=AutocompleteFormatter()).get()

class AutocompleteFormatter:
    def __init__(self):
        pass

    def format(self, records):
        formatted_records = []

        for row in records:
            label = "{0} ({1})".format(row["nombre"], row["email"])
            formatted_row = {
                "label":label,
                "value":row["id"],
                "email":row["email"]
            }

            formatted_records.append(formatted_row)

        return formatted_records