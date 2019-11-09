from model.BaseModel import BaseModel


class ModelUsuario(BaseModel):
    def __init__(self, response=None):
        super(ModelUsuario, self).__init__(response)

    def user_already_exists(self, nombre_usuario=""):
        usuario_obj = self.get_single_result(
                                            script_name="usuario_get_by_index_1",
                                            params={"nombre_usuario": nombre_usuario}
                                            )
        if usuario_obj is not None:
            self.response.add_error_msg("usuario_already_exist")
            return True
        else:
            return False

    def registrar(self, data={}):
        if not self.user_already_exists(data["nombre_usuario"]):
            stmt = self.get_query("usuario_registrar")
            usuario_id = self.execute_insert(stmt, data)
            self.response.add_info_msg("usuario_success_register")
            return usuario_id
        return None



