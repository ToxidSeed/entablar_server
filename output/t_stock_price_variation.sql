CREATE TABLE t_stock_price_variation (
FECHA_VALOR DATE,
ANYO INT,
MES INT,
DIA INT,
STOCK_SYMBOL VARCHAR(5),
DIA_SEMANA INT,
APERTURA DECIMAL(19,4),
MAXIMO DECIMAL(19,4),
MINIMO DECIMAL(19,4),
CIERRE DECIMAL(19,4),
PCT_VARIACION DECIMAL(19,4),
IND_VARIACION_POS INT,
IND_VARIACION_NEG INT
);