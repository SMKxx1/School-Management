-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: sclmgt
-- ------------------------------------------------------
-- Server version	8.0.17

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
-- Table structure for table `marks`
--

DROP TABLE IF EXISTS `marks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `std_code` varchar(45) DEFAULT NULL,
  `date_time` varchar(45) DEFAULT NULL,
  `subject` varchar(45) DEFAULT NULL,
  `marks` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marks`
--

LOCK TABLES `marks` WRITE;
/*!40000 ALTER TABLE `marks` DISABLE KEYS */;
/*!40000 ALTER TABLE `marks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(45) DEFAULT NULL,
  `question` varchar(5000) DEFAULT NULL,
  `total_marks` int(11) DEFAULT NULL,
  `date_time` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES (1,'Computers','[{\'One Word\': {\'Who is the ceo of apple?\': {\'tim cook\': \'2\'}, \'Name the co-founder of apple\': {\'steve paul jobs\': \'1\'}}}, {\'MCQ\': {\'Who made the iphone?\': {\'Apple\': {\'marks\': \'4\', \'choices\': [\'Samsung\', \'Sony\', \'Google\']}}}}, {\'True or False\': {\'Iphone runs iOS\': {True: \'1\'}}}, {\'Para\': {\'Write a short note on Steve Paul Jobs\': {\'marks\': \'5\', \'keywords\': [\'Drop out\', \'Apple\', \'Next\', \'iPhone\', \'Mac\']}}}]',13,'2019-12-02 19:34:46.208122');
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students_account`
--

DROP TABLE IF EXISTS `students_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students_account` (
  `std_id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(455) DEFAULT NULL,
  `name` varchar(455) DEFAULT NULL,
  `class` varchar(45) DEFAULT NULL,
  `sec` varchar(45) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `password` varchar(1000) DEFAULT NULL,
  `std_code` varchar(45) DEFAULT NULL,
  `log` int(11) DEFAULT '0',
  `roll_no` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`std_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students_account`
--

LOCK TABLES `students_account` WRITE;
/*!40000 ALTER TABLE `students_account` DISABLE KEYS */;
INSERT INTO `students_account` VALUES (1,'shahad.mustafa003@gmail.com','shahad','12','c','94916974','$2b$12$QusvWlQnt9/00.k5Em/QW.9gFhNoBrRH2Iti32YAPL60me1p9EGyq','$2b$12$5A037nRyYijlm6mmXaDOwO',1,NULL),(2,'shahad.mustafa@gmail.com','shahad','xii','x','749645169','$2b$12$Heb5rjbw0.Csit/ZXXJFxeZxq80ZHfOP10PXcwHY48dLf89biybXy',NULL,0,NULL),(3,'shahad@gmail.com','shahad','xii','c','894796','$2b$12$qnuFbKCiyGGwjQjQgDiVHuObHRcBbKnG9SHDPmfxWhYGIB6TU70Rq',NULL,0,NULL);
/*!40000 ALTER TABLE `students_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teachers_account`
--

DROP TABLE IF EXISTS `teachers_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teachers_account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(45) DEFAULT NULL,
  `subject` varchar(45) DEFAULT NULL,
  `password` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers_account`
--

LOCK TABLES `teachers_account` WRITE;
/*!40000 ALTER TABLE `teachers_account` DISABLE KEYS */;
INSERT INTO `teachers_account` VALUES (1,'english.teacher@gmail.com','English','$2b$12$K2dPcBeWIXWViYi0ggBu0e.0/wuxn9DzsJtkjJX0z2l7B5JFmkXRi'),(2,'maths.teacher@gmail.com','Maths','$2b$12$oG15r/cm18EwkCUNwbI.HuJOiz2sHb93B42OLkCP5ZbR8L6R.B9GK'),(3,'social.teacher@gmail.com','Social','$2b$12$t02zg5PdGtfWgfdqeU3hAeoyRgSgN.iizA4n6WzRHt/CdX23lMlhK'),(4,'science.teacher@gmail.com','Science','$2b$12$4FfGANLL6qfMHzvs/D26MecK1c1qVPNS5uklliw88Abq1KWYObguG'),(5,'computer.teacher@gmail.com','Computers','$2b$12$nVyR0k37wb2N0yJNG8rjsel7c8uCArNZW8d.UikwJpT5cRmNXsheK'),(6,'business.teacher@gmail.com','Business','$2b$12$Zfz/IDATKtdsJcgJqlpx3OEESCcb3Nyu2SJQ6svrYyJqyoYWDjo2u');
/*!40000 ALTER TABLE `teachers_account` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-02 20:10:55
