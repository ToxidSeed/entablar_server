import traceback

from domain.DomainUsuario import DomainUsuario
from helper.Response import Response
from model.ModelUsuario import ModelUsuario


class Usuario:
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


