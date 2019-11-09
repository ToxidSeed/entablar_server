select  usuario_id,
        nombre_usuario,
        nombres,
        apellidos,
        email,
        password
from usuario
where nombre_usuario = %(nombre_usuario)s
