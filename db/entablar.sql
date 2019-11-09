-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 02-11-2019 a las 11:30:21
-- Versión del servidor: 10.1.21-MariaDB
-- Versión de PHP: 7.0.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `entablar`
--
CREATE DATABASE IF NOT EXISTS `entablar` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `entablar`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `campo`
--

CREATE TABLE `campo` (
  `campo_id` int(11) NOT NULL,
  `tabla_id` int(11) DEFAULT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `descripcion` varchar(250) DEFAULT NULL,
  `flg_obligatorio` char(1) DEFAULT NULL,
  `flg_pk` char(1) DEFAULT NULL,
  `fch_creacion` date DEFAULT NULL,
  `fch_modificacion` date DEFAULT NULL,
  `tipo_dato_id` int(11) DEFAULT NULL,
  `tipo_dato_data` varchar(45) DEFAULT NULL,
  `tipo_dato_text` varchar(45) DEFAULT NULL,
  `tipo_dato_syntax` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `campo`
--

INSERT INTO `campo` (`campo_id`, `tabla_id`, `nombre`, `descripcion`, `flg_obligatorio`, `flg_pk`, `fch_creacion`, `fch_modificacion`, `tipo_dato_id`, `tipo_dato_data`, `tipo_dato_text`, `tipo_dato_syntax`) VALUES
(1, 1, 'entity_id', 'Código de Entidad con valor 0011. Parte de la llave primaria compuesta de Recaudos.\n', '0', '0', '2019-05-26', NULL, 1, '{\"p\":\"6\",\"s\":\"0\"}', 'NUMBER(6,0)', 'NUMBER(%p,%s)'),
(2, 1, 'covenant_type', 'Código de tipo de convenio con valor 001. Parte de la llave primaria compuesta de Recaudos.\n', '0', '0', '2019-05-26', NULL, 1, '{\"p\":\"4\",\"s\":\"0\"}', 'NUMBER(4,0)', 'NUMBER(%p,%s)'),
(3, 1, 'covenant_id', '', '0', '0', '2019-07-06', NULL, 0, '{}', '', ''),
(4, 3, 'category_id', 'IDENTIFICADOR DE LA CATEGORIA', '0', '0', '2019-07-14', NULL, 0, '{}', '', ''),
(5, 3, 'category_desc', '', '0', '0', '2019-07-14', NULL, 61, '{\"p\":\"8\",\"s\":\"2\"}', 'DECIMAL(8,2)', 'DECIMAL(%p,%s)'),
(6, 3, 'group_type', '', '0', '0', '2019-07-14', NULL, 59, '{}', '', 'INT'),
(7, 3, 'gl_accounting_concept_type', '', '0', '0', '2019-07-14', NULL, 74, '{\"n\":\"4\"}', 'VARCHAR(4)', 'VARCHAR(%n)'),
(8, 3, 'account_register_branch_id', '', '0', '0', '2019-07-14', NULL, 60, '{}', '', 'BIGINT'),
(9, 4, 'FECHA_VALOR', '', '0', '0', '0000-00-00', NULL, 68, '{}', 'DATE', 'DATE'),
(10, 4, 'APERTURA', '', '0', '0', '2019-07-14', NULL, 61, '{\"p\":\"19\",\"s\":\"4\"}', 'DECIMAL(19,4)', 'DECIMAL(%p,%s)'),
(11, 4, 'MAXIMO', '', '0', '0', '2019-07-14', NULL, 61, '{\"p\":\"19\",\"s\":\"4\"}', 'DECIMAL(19,4)', 'DECIMAL(%p,%s)'),
(12, 4, 'MINIMO', '', '0', '0', '2019-07-14', NULL, 61, '{\"p\":\"19\",\"s\":\"4\"}', 'DECIMAL(19,4)', 'DECIMAL(%p,%s)'),
(13, 4, 'CIERRE', '', '0', '0', '2019-07-14', NULL, 61, '{\"p\":\"19\",\"s\":\"4\"}', 'DECIMAL(19,4)', 'DECIMAL(%p,%s)'),
(14, 4, 'CIERRE_AJUSTADO', '', '0', '0', '2019-07-14', NULL, 61, '{\"p\":\"19\",\"s\":\"4\"}', 'DECIMAL(19,4)', 'DECIMAL(%p,%s)'),
(15, 4, 'VOLUMEN', '', '0', '0', '2019-07-14', NULL, 61, '{\"p\":\"19\",\"s\":\"4\"}', 'DECIMAL(19,4)', 'DECIMAL(%p,%s)'),
(17, 3, 'register_employee_id', '', '0', '0', '2019-07-14', NULL, 59, '{}', '', 'INT'),
(19, 4, 'STOCK_SYMBOL', '', '0', '0', '2019-07-14', NULL, 74, '{\"n\":\"5\"}', 'VARCHAR(5)', 'VARCHAR(%n)'),
(20, 5, 'FECHA_VALOR', '', '0', '0', '2019-07-17', NULL, 68, '{}', 'DATE', 'DATE'),
(21, 5, 'ANYO', '', '0', '0', '2019-07-17', NULL, 59, '{}', 'INT', 'INT'),
(22, 5, 'MES', '', '0', '0', '2019-07-17', NULL, 59, '{}', 'INT', 'INT'),
(23, 5, 'DIA', '', '0', '0', '2019-07-17', NULL, 59, '{}', 'INT', 'INT'),
(24, 5, 'STOCK_SYMBOL', '', '0', '0', '2019-07-17', NULL, 74, '{\"n\":\"5\"}', 'VARCHAR(5)', 'VARCHAR(%n)'),
(25, 5, 'DIA_SEMANA', '', '0', '0', '2019-07-17', NULL, 59, '{}', 'INT', 'INT'),
(26, 5, 'APERTURA', '', '0', '0', '2019-07-17', NULL, 61, '{\"p\":\"19\",\"s\":\"4\"}', 'DECIMAL(19,4)', 'DECIMAL(%p,%s)'),
(27, 5, 'MAXIMO', '', '0', '0', '2019-07-17', NULL, 61, '{\"p\":\"19\",\"s\":\"4\"}', 'DECIMAL(19,4)', 'DECIMAL(%p,%s)'),
(28, 5, 'MINIMO', '', '0', '0', '2019-07-17', NULL, 61, '{\"p\":\"19\",\"s\":\"4\"}', 'DECIMAL(19,4)', 'DECIMAL(%p,%s)'),
(29, 5, 'CIERRE', '', '0', '0', '2019-07-17', NULL, 61, '{\"p\":\"19\",\"s\":\"4\"}', 'DECIMAL(19,4)', 'DECIMAL(%p,%s)'),
(30, 5, 'PCT_VARIACION', '', '0', '0', '2019-07-17', NULL, 61, '{\"p\":\"19\",\"s\":\"4\"}', 'DECIMAL(19,4)', 'DECIMAL(%p,%s)'),
(31, 5, 'IND_VARIACION_POS', '', '0', '0', '2019-07-17', NULL, 59, '{}', 'INT', 'INT'),
(32, 5, 'IND_VARIACION_NEG', '', '0', '0', '2019-07-17', NULL, 59, '{}', 'INT', 'INT'),
(33, 7, 'CAMPO1', 'DESCRI', '0', '0', '2019-08-06', NULL, 61, '{\"p\":\"8\",\"s\":\"2\"}', 'DECIMAL(8,2)', 'DECIMAL(%p,%s)'),
(34, 7, 'CAMPO2', 'XASDAS', '0', '0', '2019-08-06', NULL, 56, '{}', 'TINYINT', 'TINYINT'),
(35, 7, 'test', 'ssss', '0', '0', '2019-08-15', NULL, 76, '{}', 'VARCHAR', 'VARCHAR'),
(36, 7, 'TEST2', 'SDSD', '0', '0', '2019-08-15', NULL, 76, '{}', 'VARCHAR', 'VARCHAR'),
(37, 1, 'CAMPO PRUEBA PK', 'DESC CAMPO PRUEBA PK', '1', '1', '2019-08-24', NULL, 1, '{\"p\":\"38\",\"s\":\"10\"}', 'NUMBER(38,10)', 'NUMBER(%p,%s)'),
(38, 1, 'CAMPO PRUEBA OBLIGATORIO', 'SSS', '1', '0', '2019-08-25', NULL, 2, '{\"n\":\"20\"}', 'VARCHAR2(20 CHAR)', 'VARCHAR2(%n CHAR)'),
(39, 28, 'estado_tabla_id', 'identificador de registro', '1', '1', '2019-08-26', NULL, 59, '{}', 'INT', 'INT'),
(40, 28, 'nombre', 'nombre del estado', '1', '0', '2019-08-26', NULL, 74, '{\"n\":\"100\"}', 'VARCHAR(100)', 'VARCHAR(%n)');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado_tabla`
--

CREATE TABLE `estado_tabla` (
  `estado_tabla_id` int(11) DEFAULT NULL,
  `nombre` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `estado_tabla`
--

INSERT INTO `estado_tabla` (`estado_tabla_id`, `nombre`) VALUES
(1, 'Activo'),
(0, 'Eliminado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedor_bd`
--

CREATE TABLE `proveedor_bd` (
  `proveedor_bd_id` int(11) NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `icono` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `proveedor_bd`
--

INSERT INTO `proveedor_bd` (`proveedor_bd_id`, `nombre`, `icono`) VALUES
(6, 'MYSQL', 'mysql.png'),
(7, 'Firebird', 'Firebird_logo_svg.png'),
(8, 'MSSQL', 'sql_server.png'),
(9, 'ORACLE', 'oracle_icon.jpg'),
(10, 'DB2', 'DB2_icon.jpg'),
(11, 'TERADATA', 'logoTeradata-Database.png'),
(12, 'POSTGRES', 'postgres.png'),
(13, 'MariaDB', 'MariaDB.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tabla`
--

CREATE TABLE `tabla` (
  `tabla_id` int(11) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `descripcion` varchar(250) DEFAULT NULL,
  `fch_creacion` date DEFAULT NULL,
  `fch_modificacion` date DEFAULT NULL,
  `dbms_id` int(11) DEFAULT NULL,
  `estado_tabla_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tabla`
--

INSERT INTO `tabla` (`tabla_id`, `nombre`, `descripcion`, `fch_creacion`, `fch_modificacion`, `dbms_id`, `estado_tabla_id`) VALUES
(1, 't_pdco_covenant', 'ssssaaaaa', '2019-05-11', '2019-08-24', 9, 0),
(3, 't_pdco_covenant_category', '', '2019-07-14', NULL, 6, 0),
(4, 't_stock_price', '', '2019-07-14', NULL, 6, 0),
(5, 't_stock_price_variation', '', '2019-07-17', NULL, 6, 0),
(6, 'dasdasddasdasd', 'asdasda', '2019-08-06', NULL, 0, 0),
(7, 'MARCELA', 'MARCELA DESCR', '2019-08-06', '0000-00-00', 6, 0),
(8, 'dsdssd', 'dsdds', '2019-08-15', NULL, 0, 0),
(9, 't_pdco_covenant', 'Código de Entidad\n', '2019-08-15', NULL, 0, 0),
(10, 't_pdco_covenant', 'Código de Entidad\nf', '2019-08-15', '2019-08-25', NULL, 0),
(11, 'TABLA_NUEVA_PRUEBA', 'TABLA_NUEVA', '2019-08-25', '2019-10-03', 0, 0),
(12, 'PRUEBA RESPONSE', 'PRUEBA RESPONSE', '2019-08-26', NULL, 0, 0),
(13, 'TABLA_PRUEBA_MENSAJE', 'TABLA_PRUEBA_MENSAJE', '2019-08-26', '2019-10-03', 0, 1),
(14, 'TABLA_PRUEBA_MENSAJE', 'TABLA_PRUEBA_MENSAJE', '2019-08-26', NULL, 0, 0),
(15, 'TABLA_PRUEBA_MENSAJE', 'TABLA_PRUEBA_MENSAJE', '2019-08-26', NULL, 0, 0),
(16, 'TABLA_PRUEBA_MENSAJE', 'TABLA_PRUEBA_MENSAJE', '2019-08-26', NULL, 0, 0),
(17, 'TABLA_PRUEBA_MENSAJE', 'TABLA_PRUEBA_MENSAJE', '2019-08-26', NULL, 0, 0),
(18, 'PRUEBA_MENSAJE_HANDLER', 'PRUEBA_MENSAJE_HANDLER', '2019-08-26', NULL, 0, 0),
(19, 'estado_tabla', 'tabla donde se guardan los estados de las tablas, estos pueden ser:\n1: Activo\n2: Eliminado\n', '2019-08-26', NULL, 0, 0),
(20, 'estado_tabla', 'Tabla donde se guardan los estados de una tabla, los valores pueden ser:\n1: Activo\n0: Eliminado', '2019-08-26', NULL, 0, 0),
(21, 'PRUEBAX', 'DESC PRUEBAX', '2019-08-26', NULL, 0, 0),
(22, 'xxxx', 'ssss', '2019-08-26', NULL, 6, 0),
(23, 'TABLA_PRUEBA', 'TABLAA_PRUEBA2', '2019-08-26', NULL, 0, 0),
(24, 'TABLA_PRUEBA2', 'TABLA_PRUEBA2', '2019-08-26', NULL, 0, 0),
(25, 'TABLAA_2', 'TABLAA_2', '2019-08-26', NULL, 0, 0),
(26, 'TABLA2', 'TABLA2', '2019-08-26', NULL, 6, 0),
(27, 'estado_tabla', 'Tabla donde se almacenan los estados de las tablas, posibles valores:\n1: Activo\n0: Eliminado', '2019-08-26', NULL, 0, 0),
(28, 'estado_tabla', 'tabla x', '2019-08-26', '2019-09-29', 6, 1),
(29, 'TABLAXX', 'TABBB', '2019-08-26', '2019-09-05', 6, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_dato`
--

CREATE TABLE `tipo_dato` (
  `tipo_dato_id` int(11) NOT NULL,
  `proveedor_bd_id` int(11) DEFAULT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `descripcion` varchar(100) DEFAULT NULL,
  `config` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `tipo_dato`
--

INSERT INTO `tipo_dato` (`tipo_dato_id`, `proveedor_bd_id`, `nombre`, `descripcion`, `config`) VALUES
(1, 9, 'NUMBER(%p,%s)', 'NUMBER', 'p(precision)=inicio:0 fin:18\ns(scale)=inicio:0 fin:8'),
(2, 9, 'VARCHAR2(%n CHAR)', '', 'n(size)=inicio:0 fin:4000'),
(56, 6, 'TINYINT', '', ''),
(57, 6, 'SMALLINT', '', ''),
(58, 6, 'MEDIUMINT', '', ''),
(59, 6, 'INT', '', ''),
(60, 6, 'BIGINT', '', ''),
(61, 6, 'DECIMAL(%p,%s)', '', 'p(precision)=inicio:0 fin:65\ns(scale)=inicio:0 fin:65'),
(62, 6, 'FLOAT(%p)', '', 'p(precision)=inicio:0 fin:53'),
(63, 6, 'FLOAT', '', ''),
(67, 6, 'BIT(%M)', '', 'M(M)=inicio:0 fin:64'),
(68, 6, 'DATE', '', ''),
(69, 6, 'TIME', '', ''),
(70, 6, 'DATETIME', '', ''),
(71, 6, 'TIMESTAMP', '', ''),
(72, 6, 'YEAR', '', ''),
(73, 6, 'CHAR(%n)', '', 'n(Tamano)=inicio:0 fin:255'),
(74, 6, 'VARCHAR(%n)', '', 'n(size)=inicio:0 fin:65535'),
(75, 6, 'CHAR', '', ''),
(76, 6, 'VARCHAR', '', ''),
(77, 7, 'VARCHAR(%n)', '', 'n(size)= inicio:0 fin:65'),
(78, 7, 'CHAR', '', '');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `campo`
--
ALTER TABLE `campo`
  ADD PRIMARY KEY (`campo_id`);

--
-- Indices de la tabla `proveedor_bd`
--
ALTER TABLE `proveedor_bd`
  ADD PRIMARY KEY (`proveedor_bd_id`);

--
-- Indices de la tabla `tabla`
--
ALTER TABLE `tabla`
  ADD PRIMARY KEY (`tabla_id`);

--
-- Indices de la tabla `tipo_dato`
--
ALTER TABLE `tipo_dato`
  ADD PRIMARY KEY (`tipo_dato_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `campo`
--
ALTER TABLE `campo`
  MODIFY `campo_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;
--
-- AUTO_INCREMENT de la tabla `proveedor_bd`
--
ALTER TABLE `proveedor_bd`
  MODIFY `proveedor_bd_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
--
-- AUTO_INCREMENT de la tabla `tabla`
--
ALTER TABLE `tabla`
  MODIFY `tabla_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;
--
-- AUTO_INCREMENT de la tabla `tipo_dato`
--
ALTER TABLE `tipo_dato`
  MODIFY `tipo_dato_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=79;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
