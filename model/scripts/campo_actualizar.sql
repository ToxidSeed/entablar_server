update campo
set tabla_id = %(tabla_id)s,
nombre = %(nombre)s,
descripcion = %(descripcion)s,
flg_obligatorio = %(flg_obligatorio)s,
flg_pk = %(flg_pk)s,
fch_creacion = %(fch_creacion)s,
tipo_dato_id = %(tipo_dato_id)s,
tipo_dato_data = %(tipo_dato_data)s,
tipo_dato_text = %(tipo_dato_text)s,
tipo_dato_syntax = %(tipo_dato_syntax)s
where campo_id = %(campo_id)s