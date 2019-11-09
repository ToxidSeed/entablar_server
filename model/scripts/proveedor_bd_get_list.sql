select proveedor_bd_id,
        nombre,
        icono
from proveedor_bd
where nombre like %s