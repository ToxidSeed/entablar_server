UPDATE TABLA
SET NOMBRE = %(nombre)s,
DESCRIPCION = %(descripcion)s,
FCH_MODIFICACION = CURRENT_DATE(),
DBMS_ID = %(dbms_id)s
WHERE TABLA_ID = %(tabla_id)s
