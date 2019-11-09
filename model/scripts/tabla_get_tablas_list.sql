SELECT tabla_id,
        nombre,
        descripcion,estado_tabla_id
        fch_creacion,
        fch_modificacion
FROM    tabla
WHERE nombre like %(nombre)s
and (estado_tabla_id in (1) or estado_tabla_id =  %(estado_tabla_id)s)
