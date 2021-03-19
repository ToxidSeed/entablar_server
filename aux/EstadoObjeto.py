from model.Estado import Estado
import aux.TipoEstado as TipoEstado
from sqlalchemy import and_

class EstadoObjeto:
    def __init__(self):
        pass

    def get(self, estado_id):
        estado = Estado.query.filter(
            and_(Estado.tipo_estado_id == TipoEstado.OBJETO,
            Estado.id == estado_id)
        ).one()

        return estado
        
