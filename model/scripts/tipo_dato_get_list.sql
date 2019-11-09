SELECT tipo_dato_id,
        proveedor_bd_id,
        nombre,
        descripcion,
        config
FROM    tipo_dato
WHERE proveedor_bd_id = %s
 and nombre like %s