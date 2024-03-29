CREATE DATABASE  IF NOT EXISTS `datasiswa` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `datasiswa`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: datasiswa
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `nilaibahasa`
--

DROP TABLE IF EXISTS `nilaibahasa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nilaibahasa` (
  `Kode_Nilai` int NOT NULL,
  `ID_Siswa` int DEFAULT NULL,
  `Antropologi` int DEFAULT NULL,
  `Bahasa_Indonesia` int DEFAULT NULL,
  `Bahasa_Jepang` int DEFAULT NULL,
  `Bahasa_Inggris` int DEFAULT NULL,
  PRIMARY KEY (`Kode_Nilai`),
  KEY `ID_Siswa` (`ID_Siswa`),
  CONSTRAINT `nilaibahasa_ibfk_1` FOREIGN KEY (`ID_Siswa`) REFERENCES `bahasa` (`ID_Siswa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nilaibahasa`
--

LOCK TABLES `nilaibahasa` WRITE;
/*!40000 ALTER TABLE `nilaibahasa` DISABLE KEYS */;
INSERT INTO `nilaibahasa` VALUES (10310,100301,75,60,85,95),(10311,110301,85,60,95,75),(10312,120301,80,70,95,85),(20310,100302,70,87,80,85),(20311,110302,80,87,90,95),(20312,120302,88,77,90,75),(30310,100303,80,97,90,95),(30311,110303,70,97,80,85),(30312,120303,90,77,80,85),(40310,100304,90,80,95,75),(40311,110304,70,80,80,95),(40312,120304,77,80,90,65);
/*!40000 ALTER TABLE `nilaibahasa` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-30 21:46:18
