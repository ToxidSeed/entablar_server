-- MariaDB dump 10.18  Distrib 10.5.8-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: entablar
-- ------------------------------------------------------
-- Server version	10.5.8-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `base_datos`
--

DROP TABLE IF EXISTS `base_datos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `base_datos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(250) NOT NULL,
  `dbms_id` int(11) DEFAULT NULL,
  `fch_creacion` date NOT NULL,
  `desc_abreviada` varchar(50) DEFAULT NULL,
  `desc_completa` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_datos`
--

LOCK TABLES `base_datos` WRITE;
/*!40000 ALTER TABLE `base_datos` DISABLE KEYS */;
/*!40000 ALTER TABLE `base_datos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `campo`
--

DROP TABLE IF EXISTS `campo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `campo` (
  `campo_id` int(11) NOT NULL AUTO_INCREMENT,
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
  `tipo_dato_syntax` varchar(45) DEFAULT NULL,
  `desc_abreviada` varchar(50) DEFAULT NULL,
  `desc_completa` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`campo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `campo`
--

LOCK TABLES `campo` WRITE;
/*!40000 ALTER TABLE `campo` DISABLE KEYS */;
INSERT INTO `campo` VALUES (1,1,'entity_id','Código de Entidad con valor 0011. Parte de la llave primaria compuesta de Recaudos.\n','0','0','2019-05-26',NULL,1,'{\"p\":\"6\",\"s\":\"0\"}','NUMBER(6,0)','NUMBER(%p,%s)',NULL,NULL),(2,1,'covenant_type','Código de tipo de convenio con valor 001. Parte de la llave primaria compuesta de Recaudos.\n','0','0','2019-05-26',NULL,1,'{\"p\":\"4\",\"s\":\"0\"}','NUMBER(4,0)','NUMBER(%p,%s)',NULL,NULL),(3,1,'covenant_id','','0','0','2019-07-06',NULL,0,'{}','','',NULL,NULL),(4,3,'category_id','IDENTIFICADOR DE LA CATEGORIA','0','0','2019-07-14',NULL,0,'{}','','',NULL,NULL),(5,3,'category_desc','','0','0','2019-07-14',NULL,61,'{\"p\":\"8\",\"s\":\"2\"}','DECIMAL(8,2)','DECIMAL(%p,%s)',NULL,NULL),(6,3,'group_type','','0','0','2019-07-14',NULL,59,'{}','','INT',NULL,NULL),(7,3,'gl_accounting_concept_type','','0','0','2019-07-14',NULL,74,'{\"n\":\"4\"}','VARCHAR(4)','VARCHAR(%n)',NULL,NULL),(8,3,'account_register_branch_id','','0','0','2019-07-14',NULL,60,'{}','','BIGINT',NULL,NULL),(9,4,'FECHA_VALOR','','0','0','0000-00-00',NULL,68,'{}','DATE','DATE',NULL,NULL),(10,4,'APERTURA','','0','0','2019-07-14',NULL,61,'{\"p\":\"19\",\"s\":\"4\"}','DECIMAL(19,4)','DECIMAL(%p,%s)',NULL,NULL),(11,4,'MAXIMO','','0','0','2019-07-14',NULL,61,'{\"p\":\"19\",\"s\":\"4\"}','DECIMAL(19,4)','DECIMAL(%p,%s)',NULL,NULL),(12,4,'MINIMO','','0','0','2019-07-14',NULL,61,'{\"p\":\"19\",\"s\":\"4\"}','DECIMAL(19,4)','DECIMAL(%p,%s)',NULL,NULL),(13,4,'CIERRE','','0','0','2019-07-14',NULL,61,'{\"p\":\"19\",\"s\":\"4\"}','DECIMAL(19,4)','DECIMAL(%p,%s)',NULL,NULL),(14,4,'CIERRE_AJUSTADO','','0','0','2019-07-14',NULL,61,'{\"p\":\"19\",\"s\":\"4\"}','DECIMAL(19,4)','DECIMAL(%p,%s)',NULL,NULL),(15,4,'VOLUMEN','','0','0','2019-07-14',NULL,61,'{\"p\":\"19\",\"s\":\"4\"}','DECIMAL(19,4)','DECIMAL(%p,%s)',NULL,NULL),(17,3,'register_employee_id','','0','0','2019-07-14',NULL,59,'{}','','INT',NULL,NULL),(19,4,'STOCK_SYMBOL','','0','0','2019-07-14',NULL,74,'{\"n\":\"5\"}','VARCHAR(5)','VARCHAR(%n)',NULL,NULL),(20,5,'FECHA_VALOR','','0','0','2019-07-17',NULL,68,'{}','DATE','DATE',NULL,NULL),(21,5,'ANYO','','0','0','2019-07-17',NULL,59,'{}','INT','INT',NULL,NULL),(22,5,'MES','','0','0','2019-07-17',NULL,59,'{}','INT','INT',NULL,NULL),(23,5,'DIA','','0','0','2019-07-17',NULL,59,'{}','INT','INT',NULL,NULL),(24,5,'STOCK_SYMBOL','','0','0','2019-07-17',NULL,74,'{\"n\":\"5\"}','VARCHAR(5)','VARCHAR(%n)',NULL,NULL),(25,5,'DIA_SEMANA','','0','0','2019-07-17',NULL,59,'{}','INT','INT',NULL,NULL),(26,5,'APERTURA','','0','0','2019-07-17',NULL,61,'{\"p\":\"19\",\"s\":\"4\"}','DECIMAL(19,4)','DECIMAL(%p,%s)',NULL,NULL),(27,5,'MAXIMO','','0','0','2019-07-17',NULL,61,'{\"p\":\"19\",\"s\":\"4\"}','DECIMAL(19,4)','DECIMAL(%p,%s)',NULL,NULL),(28,5,'MINIMO','','0','0','2019-07-17',NULL,61,'{\"p\":\"19\",\"s\":\"4\"}','DECIMAL(19,4)','DECIMAL(%p,%s)',NULL,NULL),(29,5,'CIERRE','','0','0','2019-07-17',NULL,61,'{\"p\":\"19\",\"s\":\"4\"}','DECIMAL(19,4)','DECIMAL(%p,%s)',NULL,NULL),(30,5,'PCT_VARIACION','','0','0','2019-07-17',NULL,61,'{\"p\":\"19\",\"s\":\"4\"}','DECIMAL(19,4)','DECIMAL(%p,%s)',NULL,NULL),(31,5,'IND_VARIACION_POS','','0','0','2019-07-17',NULL,59,'{}','INT','INT',NULL,NULL),(32,5,'IND_VARIACION_NEG','','0','0','2019-07-17',NULL,59,'{}','INT','INT',NULL,NULL),(33,7,'CAMPO1','DESCRI','0','0','2019-08-06',NULL,61,'{\"p\":\"8\",\"s\":\"2\"}','DECIMAL(8,2)','DECIMAL(%p,%s)',NULL,NULL),(34,7,'CAMPO2','XASDAS','0','0','2019-08-06',NULL,56,'{}','TINYINT','TINYINT',NULL,NULL),(35,7,'test','ssss','0','0','2019-08-15',NULL,76,'{}','VARCHAR','VARCHAR',NULL,NULL),(36,7,'TEST2','SDSD','0','0','2019-08-15',NULL,76,'{}','VARCHAR','VARCHAR',NULL,NULL),(37,1,'CAMPO PRUEBA PK','DESC CAMPO PRUEBA PK','1','1','2019-08-24',NULL,1,'{\"p\":\"38\",\"s\":\"10\"}','NUMBER(38,10)','NUMBER(%p,%s)',NULL,NULL),(38,1,'CAMPO PRUEBA OBLIGATORIO','SSS','1','0','2019-08-25',NULL,2,'{\"n\":\"20\"}','VARCHAR2(20 CHAR)','VARCHAR2(%n CHAR)',NULL,NULL),(39,28,'estado_tabla_id','identificador de registro','1','1','2019-08-26',NULL,59,'{}','INT','INT',NULL,NULL),(40,28,'nombre','nombre del estado','1','0','2019-08-26',NULL,74,'{\"n\":\"100\"}','VARCHAR(100)','VARCHAR(%n)',NULL,NULL);
/*!40000 ALTER TABLE `campo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estado`
--

DROP TABLE IF EXISTS `estado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `estado` (
  `id` int(11) NOT NULL,
  `tipo_estado_id` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`,`tipo_estado_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado`
--

LOCK TABLES `estado` WRITE;
/*!40000 ALTER TABLE `estado` DISABLE KEYS */;
INSERT INTO `estado` VALUES (0,1,'Borrador'),(1,1,'Enviado a Aprobar'),(2,1,'Aprobado'),(3,1,'eliminado');
/*!40000 ALTER TABLE `estado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `objeto`
--

DROP TABLE IF EXISTS `objeto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `objeto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(250) DEFAULT NULL,
  `tipo_objeto_id` int(11) DEFAULT NULL,
  `dbms_id` int(11) DEFAULT NULL,
  `desc_abreviada` varchar(250) DEFAULT NULL,
  `desc_completa` varchar(500) DEFAULT NULL,
  `estado_id` int(11) DEFAULT NULL,
  `fch_creacion` date DEFAULT NULL,
  `fch_modificacion` date DEFAULT NULL,
  `objeto_padre_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `objeto`
--

LOCK TABLES `objeto` WRITE;
/*!40000 ALTER TABLE `objeto` DISABLE KEYS */;
INSERT INTO `objeto` VALUES (1,'nombre x',2,11,'desc abrev','desc comple',3,'2021-02-07','2021-02-07',NULL),(2,'NOMBRE X',2,11,'DESC ABREV','DESC COMPLE',3,'2021-02-07','2021-02-07',NULL),(3,'NUEVA_TABLA',2,11,'DESC ABRE','DESC COMPLE',0,'2021-02-07','2021-02-07',NULL),(4,'TKIDSHGM',1,6,NULL,NULL,0,'2021-02-13','2021-02-13',NULL),(5,'sss',1,11,NULL,NULL,0,'2021-02-13','2021-02-13',NULL),(6,'entablar',1,6,NULL,NULL,0,'2021-02-13','2021-02-13',NULL),(7,'KIDSH',4,6,NULL,NULL,4,'2021-02-20','2021-02-20',4),(8,'LAGARTO',1,6,NULL,NULL,0,'2021-02-20','2021-02-20',NULL),(9,'MAPACHE',1,6,NULL,NULL,0,'2021-02-20','2021-02-20',NULL),(10,'LAGARTO TERA',1,11,NULL,NULL,0,'2021-02-20','2021-02-20',NULL),(11,'BD_REPTILES_TERA',1,11,NULL,NULL,0,'2021-02-20','2021-02-20',NULL),(12,'ESQ_SERPIENTES_TERA',4,11,NULL,NULL,4,'2021-02-20','2021-02-20',11),(13,'ESQ_LAGARTOS_TERA',4,11,NULL,NULL,4,'2021-02-20','2021-02-20',11),(14,'ESQ_GECKOS_TERA',4,11,NULL,NULL,4,'2021-02-20','2021-02-20',11),(15,'TB_MAMBA_NEGRA',2,11,'tabla que almacena los datos de la serpiente mamba negra','',0,'2021-02-21','2021-02-21',NULL),(16,'TB_TAIPAN',2,11,'serpiente australiana muy venenosa','',0,'2021-02-21','2021-02-21',NULL),(17,'TB_KRAIT',2,11,'SERPIENTE VENENOSA DE ASIA','',0,'2021-02-21','2021-02-21',12),(18,'TB_BARANO',2,11,'TABLA DONDE SE VAN A ALMACENAR LOS DATOS DE BARANO','',3,'2021-02-21','2021-02-21',13),(19,NULL,3,11,'','desc completa campo',0,'2021-03-21',NULL,17),(20,NULL,3,11,'','desc completa campo',0,'2021-03-21',NULL,17),(21,'CAMPO1',3,11,'','desc completa campo',0,'2021-03-21',NULL,17),(24,'CAMPO2',3,11,'','desc completa campo',0,'2021-03-21',NULL,17),(25,'CAMPO3',3,11,'','desc completa campo',0,'2021-03-21',NULL,17);
/*!40000 ALTER TABLE `objeto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `objeto_props`
--

DROP TABLE IF EXISTS `objeto_props`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `objeto_props` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `objeto_id` int(11) DEFAULT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `valor` varchar(250) DEFAULT NULL,
  `fch_creacion` date DEFAULT NULL,
  `fch_modificacion` date DEFAULT NULL,
  `flg_activo` char(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `objeto_props`
--

LOCK TABLES `objeto_props` WRITE;
/*!40000 ALTER TABLE `objeto_props` DISABLE KEYS */;
INSERT INTO `objeto_props` VALUES (1,15,'DATABASE_ID','11','2021-02-21','2021-02-21',NULL),(2,15,'ESQUEMA_ID','12','2021-02-21','2021-02-21',NULL),(3,16,'DATABASE_ID','11','2021-02-21','2021-02-21',NULL),(4,16,'ESQUEMA_ID','12','2021-02-21','2021-02-21',NULL),(5,17,'DATABASE_ID','11','2021-02-21','2021-02-21',NULL),(6,18,'DATABASE_ID','11','2021-02-21','2021-02-21',NULL),(7,24,'TIPO_DATO_ID','79',NULL,NULL,NULL),(8,24,'n','20',NULL,NULL,NULL),(9,25,'TIPO_DATO_ID','79','2021-03-21',NULL,'S'),(10,25,'n','20','2021-03-21',NULL,'S');
/*!40000 ALTER TABLE `objeto_props` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedor_bd`
--

DROP TABLE IF EXISTS `proveedor_bd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `proveedor_bd` (
  `proveedor_bd_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `icono` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`proveedor_bd_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedor_bd`
--

LOCK TABLES `proveedor_bd` WRITE;
/*!40000 ALTER TABLE `proveedor_bd` DISABLE KEYS */;
INSERT INTO `proveedor_bd` VALUES (6,'MYSQL','mysql.png'),(7,'Firebird','Firebird_logo_svg.png'),(8,'MSSQL','sql_server.png'),(9,'ORACLE','oracle_icon.jpg'),(10,'DB2','DB2_icon.jpg'),(11,'TERADATA','logoTeradata-Database.png'),(12,'POSTGRES','postgres.png'),(13,'MariaDB','MariaDB.png');
/*!40000 ALTER TABLE `proveedor_bd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tabla`
--

DROP TABLE IF EXISTS `tabla`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tabla` (
  `tabla_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `descripcion` varchar(250) DEFAULT NULL,
  `fch_creacion` date DEFAULT NULL,
  `fch_modificacion` date DEFAULT NULL,
  `dbms_id` int(11) DEFAULT NULL,
  `estado_tabla_id` int(11) DEFAULT NULL,
  `desc_abreviada` varchar(50) DEFAULT NULL,
  `desc_completa` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`tabla_id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tabla`
--

LOCK TABLES `tabla` WRITE;
/*!40000 ALTER TABLE `tabla` DISABLE KEYS */;
INSERT INTO `tabla` VALUES (1,'t_pdco_covenant','ssssaaaaa','2019-05-11','2019-08-24',9,0,NULL,NULL),(3,'t_pdco_covenant_category','','2019-07-14',NULL,6,0,NULL,NULL),(4,'t_stock_price','','2019-07-14',NULL,6,0,NULL,NULL),(5,'t_stock_price_variation','','2019-07-17',NULL,6,0,NULL,NULL),(6,'dasdasddasdasd','asdasda','2019-08-06',NULL,0,0,NULL,NULL),(7,'MARCELA','MARCELA DESCR','2019-08-06','0000-00-00',6,0,NULL,NULL),(8,'dsdssd','dsdds','2019-08-15',NULL,0,0,NULL,NULL),(9,'t_pdco_covenant','Código de Entidad\n','2019-08-15',NULL,0,0,NULL,NULL),(10,'t_pdco_covenant','Código de Entidad\nf','2019-08-15','2019-08-25',NULL,0,NULL,NULL),(11,'TABLA_NUEVA_PRUEBA','TABLA_NUEVA','2019-08-25','2019-10-03',0,0,NULL,NULL),(12,'PRUEBA RESPONSE','PRUEBA RESPONSE','2019-08-26',NULL,0,0,NULL,NULL),(13,'TABLA_PRUEBA_MENSAJE','TABLA_PRUEBA_MENSAJE','2019-08-26','2019-10-03',0,1,NULL,NULL),(14,'TABLA_PRUEBA_MENSAJE','TABLA_PRUEBA_MENSAJE','2019-08-26',NULL,0,0,NULL,NULL),(15,'TABLA_PRUEBA_MENSAJE','TABLA_PRUEBA_MENSAJE','2019-08-26',NULL,0,0,NULL,NULL),(16,'TABLA_PRUEBA_MENSAJE','TABLA_PRUEBA_MENSAJE','2019-08-26',NULL,0,0,NULL,NULL),(17,'TABLA_PRUEBA_MENSAJE','TABLA_PRUEBA_MENSAJE','2019-08-26',NULL,0,0,NULL,NULL),(18,'PRUEBA_MENSAJE_HANDLER','PRUEBA_MENSAJE_HANDLER','2019-08-26',NULL,0,0,NULL,NULL),(19,'estado_tabla','tabla donde se guardan los estados de las tablas, estos pueden ser:\n1: Activo\n2: Eliminado\n','2019-08-26',NULL,0,0,NULL,NULL),(20,'estado_tabla','Tabla donde se guardan los estados de una tabla, los valores pueden ser:\n1: Activo\n0: Eliminado','2019-08-26',NULL,0,0,NULL,NULL),(21,'PRUEBAX','DESC PRUEBAX','2019-08-26',NULL,0,0,NULL,NULL),(22,'xxxx','ssss','2019-08-26',NULL,6,0,NULL,NULL),(23,'TABLA_PRUEBA','TABLAA_PRUEBA2','2019-08-26',NULL,0,0,NULL,NULL),(24,'TABLA_PRUEBA2','TABLA_PRUEBA2','2019-08-26',NULL,0,0,NULL,NULL),(25,'TABLAA_2','TABLAA_2','2019-08-26',NULL,0,0,NULL,NULL),(26,'TABLA2','TABLA2','2019-08-26',NULL,6,0,NULL,NULL),(27,'estado_tabla','Tabla donde se almacenan los estados de las tablas, posibles valores:\n1: Activo\n0: Eliminado','2019-08-26',NULL,0,0,NULL,NULL),(28,'estado_tabla','tabla x','2019-08-26','2019-09-29',6,1,NULL,NULL),(29,'TABLAXX','TABBB','2019-08-26','2019-09-05',6,0,NULL,NULL);
/*!40000 ALTER TABLE `tabla` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_dato`
--

DROP TABLE IF EXISTS `tipo_dato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_dato` (
  `tipo_dato_id` int(11) NOT NULL AUTO_INCREMENT,
  `proveedor_bd_id` int(11) DEFAULT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  `descripcion` varchar(100) DEFAULT NULL,
  `config` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`tipo_dato_id`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_dato`
--

LOCK TABLES `tipo_dato` WRITE;
/*!40000 ALTER TABLE `tipo_dato` DISABLE KEYS */;
INSERT INTO `tipo_dato` VALUES (1,9,'NUMBER(%p,%s)','NUMBER','p(precision)=inicio:0 fin:18\ns(scale)=inicio:0 fin:8'),(2,9,'VARCHAR2(%n CHAR)','','n(size)=inicio:0 fin:4000'),(56,6,'TINYINT','',''),(57,6,'SMALLINT','',''),(58,6,'MEDIUMINT','',''),(59,6,'INT','',''),(60,6,'BIGINT','',''),(61,6,'DECIMAL(%p,%s)','','p(precision)=inicio:0 fin:65\ns(scale)=inicio:0 fin:65'),(62,6,'FLOAT(%p)','','p(precision)=inicio:0 fin:53'),(63,6,'FLOAT','',''),(67,6,'BIT(%M)','','M(M)=inicio:0 fin:64'),(68,6,'DATE','',''),(69,6,'TIME','',''),(70,6,'DATETIME','',''),(71,6,'TIMESTAMP','',''),(72,6,'YEAR','',''),(73,6,'CHAR(%n)','','n(Tamano)=inicio:0 fin:255'),(74,6,'VARCHAR(%n)','','n(size)=inicio:0 fin:65535'),(75,6,'CHAR','',''),(76,6,'VARCHAR','',''),(77,7,'VARCHAR(%n)','','n(size)= inicio:0 fin:65'),(78,7,'CHAR','',''),(79,11,'VARCHAR(%n)','descripcion','var:n,desc:número de caracteres,inicio:1, fin:64000'),(80,11,'CHARACTER(%n)','tipo de datos char','var:n,desc:número de caracteres,inicio:1,fin:64000'),(81,11,'BYTEINT','BYTEINT','');
/*!40000 ALTER TABLE `tipo_dato` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_estado`
--

DROP TABLE IF EXISTS `tipo_estado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_estado` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_estado`
--

LOCK TABLES `tipo_estado` WRITE;
/*!40000 ALTER TABLE `tipo_estado` DISABLE KEYS */;
INSERT INTO `tipo_estado` VALUES (1,'objetos');
/*!40000 ALTER TABLE `tipo_estado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_objeto`
--

DROP TABLE IF EXISTS `tipo_objeto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_objeto` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `NOMBRE` varchar(100) DEFAULT NULL,
  `ICONO` varchar(100) DEFAULT NULL,
  `FCH_CREACION` date DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_objeto`
--

LOCK TABLES `tipo_objeto` WRITE;
/*!40000 ALTER TABLE `tipo_objeto` DISABLE KEYS */;
INSERT INTO `tipo_objeto` VALUES (1,'base de datos',NULL,NULL),(2,'tabla',NULL,NULL),(3,'campo',NULL,NULL),(4,'Esquema','','2021-06-02');
/*!40000 ALTER TABLE `tipo_objeto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `descripcion` varchar(250) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `provider` varchar(20) DEFAULT NULL,
  `fch_creacion` date DEFAULT NULL,
  `confirmado` tinyint(1) DEFAULT NULL,
  `fch_confirmacion` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (18,'Miguel Angel Quispe Conde',NULL,NULL,'miguel.angel.cuarez@gmail.com','google','2020-12-13',1,'2020-12-13');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `v_objeto`
--

DROP TABLE IF EXISTS `v_objeto`;
/*!50001 DROP VIEW IF EXISTS `v_objeto`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_objeto` (
  `id` tinyint NOT NULL,
  `tipo_objeto_id` tinyint NOT NULL,
  `nombre` tinyint NOT NULL,
  `desc_abreviada` tinyint NOT NULL,
  `desc_completa` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `v_objeto`
--

/*!50001 DROP TABLE IF EXISTS `v_objeto`*/;
/*!50001 DROP VIEW IF EXISTS `v_objeto`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`osboxes`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_objeto` AS select `base_datos`.`id` AS `id`,1 AS `tipo_objeto_id`,`base_datos`.`nombre` AS `nombre`,`base_datos`.`desc_abreviada` AS `desc_abreviada`,`base_datos`.`desc_completa` AS `desc_completa` from `base_datos` union all select `tabla`.`tabla_id` AS `id`,2 AS `tipo_objeto_id`,`tabla`.`nombre` AS `nombre`,`tabla`.`desc_abreviada` AS `desc_abreviada`,`tabla`.`desc_completa` AS `desc_completa` from `tabla` union all select `campo`.`campo_id` AS `id`,3 AS `tipo_objeto_id`,`campo`.`nombre` AS `nombre`,`campo`.`desc_abreviada` AS `desc_abreviada`,`campo`.`desc_completa` AS `desc_completa` from `campo` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-28 15:37:51
