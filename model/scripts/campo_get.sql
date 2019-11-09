select campo_id,
        tabla_id,
        nombre,
        descripcion,
        flg_obligatorio,
        flg_pk,
        fch_creacion,
        fch_modificacion,
        tipo_dato_id,
        tipo_dato_data,
        tipo_dato_text,
        tipo_dato_syntax
from campo
where campo_id = %s