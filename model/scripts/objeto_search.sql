select id, 
tipo_objeto_id,
nombre,
desc_abreviada,
desc_completa
from v_objeto
where nombre like %(search_text)s or desc_abreviada like %(search_text)s or desc_completa like %(search_text)s
