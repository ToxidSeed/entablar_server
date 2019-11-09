INSERT INTO usuario
(
nombre_usuario,
nombres,
apellidos,
password
)
VALUES(
%(nombre_usuario)s,
%(nombres)s,
%(apellidos)s,
%(password)s
)
