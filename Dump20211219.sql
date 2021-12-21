-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: test
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cadet`
--

DROP TABLE IF EXISTS `cadet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cadet` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cadet`
--

LOCK TABLES `cadet` WRITE;
/*!40000 ALTER TABLE `cadet` DISABLE KEYS */;
INSERT INTO `cadet` VALUES (1,'Пивнев Кирилл'),(2,'Потапов Данила'),(3,'Прокофьев Данила'),(4,'Склянин Владимир'),(5,'Солодянкин Егор'),(6,'Сорвачев Дмитрий'),(7,'Сорокин Даниил'),(8,'Тимичев Анатолий'),(9,'Токунов Иван'),(10,'Чирков Матвей'),(12,'Безруков Игорь'),(13,'Быков Илья'),(14,'Галкин Кирилл'),(15,'Дериглазов Антон'),(16,'Драгунов Алексей'),(17,'Еретин Даниил'),(18,'Калешманов Тимофей'),(19,'Крысин Артем'),(20,'Левин Владислав'),(21,'Меркульев Евгений'),(22,'Наумов Артем'),(23,'Недзимовский Роман'),(24,'Омельянович Павел'),(25,'Плешков Кирилл'),(26,'Ругалев Артем'),(27,'Самсонов Павел'),(28,'Хомутов Владислав'),(29,'Шеварев Владимир'),(30,'Шолин Дмитрий'),(31,'Анисимов Даниил'),(32,'Балинов Максим'),(33,'Благов Даниил'),(34,'Бобков Андрей'),(35,'Богатов Леонид'),(36,'Валюгин Михаил'),(37,'Данилов Павел'),(38,'Дерюгин Матвей'),(39,'Кирилов Владимир'),(40,'Колоколов Дмитрий'),(41,'Комиссаров Александр'),(42,'Кочинов Владислав'),(43,'Кулешов Алексей'),(44,'Лыков Владимир'),(45,'Мельников Никита'),(46,'Мочалов Дмитрий'),(47,'Мурзин Дмитрий'),(48,'Мыльников Иван'),(49,'Самойлов Никита'),(50,'Спирин Вячеслав'),(51,'Филимонов Никита'),(54,'Ануфриев Александр'),(57,'Ануфриев Александр'),(62,'Андронов Алексей');
/*!40000 ALTER TABLE `cadet` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `del_cadet` BEFORE DELETE ON `cadet` FOR EACH ROW delete from cadet_print where name = old.name */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `cadet_print`
--

DROP TABLE IF EXISTS `cadet_print`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cadet_print` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cadet_print`
--

LOCK TABLES `cadet_print` WRITE;
/*!40000 ALTER TABLE `cadet_print` DISABLE KEYS */;
INSERT INTO `cadet_print` VALUES (3,'Ануфриев Александр');
/*!40000 ALTER TABLE `cadet_print` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-19 21:11:35
