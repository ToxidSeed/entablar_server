INSERT INTO USUARIO
(
usuario_id,
nombre_usuario,
nombres,
apellidos,
password
)
VALUES
(
%(usuario_id)s,
%(nombre_usuario)s,
%(nombres)s,
%(apellidos)s,
%(password)
)