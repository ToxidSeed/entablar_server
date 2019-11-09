select  tipo_dato_id,
        proveedor_bd_id,
        nombre,
        descripcion,
        config
from tipo_dato
where tipo_dato_id = %s