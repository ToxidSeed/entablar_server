SELECT
campo_id,
tabla_id,
nombre,
descripcion,
tipo_dato_id,
tipo_dato_data,
tipo_dato_text,
tipo_dato_syntax,
flg_obligatorio,
flg_pk,
fch_creacion,
fch_modificacion
FROM campo
WHERE tabla_id = %s