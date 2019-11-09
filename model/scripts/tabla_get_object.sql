SELECT tabla_id,
        nombre,
        descripcion,
        fch_creacion,
        fch_modificacion,
        dbms_id,
        estado_tabla_id
FROM    tabla
WHERE tabla_id = %s