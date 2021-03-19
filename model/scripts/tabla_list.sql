select 
tabla.id, 
tabla.nombre,
tabla.dbms_id,
proveedor_bd.nombre as dbms_nombre,
tabla.desc_abreviada,
tabla.desc_completa,
tabla.estado_id,
estado.nombre as estado_nombre,
tabla.fch_creacion ,
tabla.fch_modificacion ,
tabla.objeto_padre_id ,
esquema.id as esquema_id,
esquema.nombre as esquema_nombre,
db_props.valor as database_id,
db.nombre as database_nombre
from objeto tabla 
	left join proveedor_bd
on tabla.dbms_id = proveedor_bd.proveedor_bd_id	
	left join estado
on tabla.estado_id = estado.id
and estado.tipo_estado_id = 1
	left join objeto esquema
on tabla.objeto_padre_id = esquema.id
	left join objeto_props db_props
on tabla.id = db_props.objeto_id 
and db_props.nombre = 'DATABASE_ID'
	left join objeto db
on db_props.valor = db.id
where tabla.tipo_objeto_id = 2
and (
tabla.nombre like '%{search_text}%' or
tabla.desc_abreviada like '%{search_text}%' or
tabla.desc_completa like '%{search_text}%'
)
