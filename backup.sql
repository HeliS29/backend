-- MySQL dump 10.13  Distrib 8.0.40, for Linux (x86_64)
--
-- Host: localhost    Database: activate
-- ------------------------------------------------------
-- Server version	8.0.40-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `report_version_id` int NOT NULL,
  `comment_text` text NOT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `report_version_id` (`report_version_id`),
  KEY `ix_comments_id` (`id`),
  CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `comments_ibfk_2` FOREIGN KEY (`report_version_id`) REFERENCES `report_versions` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (1,4,1,'first report from backend server','2025-01-08 04:34:59'),(2,2,6,'user first version','2025-01-08 07:12:23'),(3,2,7,'third version','2025-01-08 07:34:57'),(4,2,8,'fourth version','2025-01-08 07:40:11'),(5,1,9,'root user first report','2025-01-08 10:09:15'),(6,1,10,'Second version by user','2025-01-08 10:24:46'),(7,1,11,'Third version for frontend and backend by user','2025-01-08 11:12:53'),(8,1,12,'approved by manager','2025-01-08 11:23:16'),(9,6,13,'first version','2025-01-08 12:33:56'),(10,16,14,'This1st version report viewed by manager','2025-01-08 13:24:04'),(11,12,15,'axskmkmk','2025-01-08 13:28:53'),(12,12,16,'adasds','2025-01-08 13:32:25'),(13,18,17,'this is1st version viewed by manager','2025-01-08 13:44:59'),(14,18,18,'2nd version','2025-01-09 04:29:17'),(15,18,19,'By Manager: 3rd version, with data science and ai','2025-01-09 04:34:20'),(16,10,20,'1st report version','2025-01-09 04:40:37');
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_focus_areas`
--

DROP TABLE IF EXISTS `core_focus_areas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_focus_areas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `area` varchar(100) NOT NULL,
  `time_spent` float NOT NULL,
  `importance` float NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `core_focus_areas_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_focus_areas`
--

LOCK TABLES `core_focus_areas` WRITE;
/*!40000 ALTER TABLE `core_focus_areas` DISABLE KEYS */;
INSERT INTO `core_focus_areas` VALUES (31,2,'frontend',50,50,'2025-01-08 07:36:45','2025-01-08 07:36:45'),(32,2,'backend',50,50,'2025-01-08 07:36:45','2025-01-08 07:36:45'),(46,1,'test',100,100,'2025-01-08 11:34:57','2025-01-08 11:34:57'),(47,6,'frontend',40,50,'2025-01-08 12:33:01','2025-01-08 12:33:01'),(48,6,'backend',60,50,'2025-01-08 12:33:01','2025-01-08 12:33:01'),(49,16,'Marketing',20,30,'2025-01-08 13:20:17','2025-01-08 13:20:17'),(50,16,'Finance',30,30,'2025-01-08 13:20:17','2025-01-08 13:20:17'),(51,16,'HR',30,25,'2025-01-08 13:20:17','2025-01-08 13:20:17'),(52,16,'BDE',20,15,'2025-01-08 13:20:17','2025-01-08 13:20:17'),(62,18,'data science',50,50,'2025-01-09 04:30:50','2025-01-09 04:30:50'),(63,18,'AI',50,50,'2025-01-09 04:30:50','2025-01-09 04:30:50'),(64,10,'frontend',40,40,'2025-01-09 04:38:53','2025-01-09 04:38:53'),(65,10,'backend',60,60,'2025-01-09 04:38:53','2025-01-09 04:38:53'),(66,12,'frontend',100,100,'2025-01-09 09:59:47','2025-01-09 09:59:47');
/*!40000 ALTER TABLE `core_focus_areas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `critical_activities`
--

DROP TABLE IF EXISTS `critical_activities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `critical_activities` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `core_focus_area_id` int NOT NULL,
  `area` varchar(100) NOT NULL,
  `importance` float NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `critical_activities_ibfk_2` (`core_focus_area_id`),
  CONSTRAINT `critical_activities_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `critical_activities_ibfk_2` FOREIGN KEY (`core_focus_area_id`) REFERENCES `core_focus_areas` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=183 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `critical_activities`
--

LOCK TABLES `critical_activities` WRITE;
/*!40000 ALTER TABLE `critical_activities` DISABLE KEYS */;
INSERT INTO `critical_activities` VALUES (85,2,31,'www',100,'2025-01-08 07:36:56','2025-01-08 07:36:56'),(86,2,32,'www2',100,'2025-01-08 07:36:56','2025-01-08 07:36:56'),(121,1,46,'test',100,'2025-01-08 11:35:02','2025-01-08 11:35:02'),(122,6,47,'html',30,'2025-01-08 12:33:23','2025-01-08 12:33:23'),(123,6,47,'api integrations',30,'2025-01-08 12:33:23','2025-01-08 12:33:23'),(124,6,47,'js',40,'2025-01-08 12:33:23','2025-01-08 12:33:23'),(125,6,48,'database',30,'2025-01-08 12:33:23','2025-01-08 12:33:23'),(126,6,48,'apis',30,'2025-01-08 12:33:23','2025-01-08 12:33:23'),(127,6,48,'testing',30,'2025-01-08 12:33:23','2025-01-08 12:33:23'),(128,16,49,'SEO optimization',30,'2025-01-08 13:23:28','2025-01-08 13:23:28'),(129,16,49,'digital marketing',20,'2025-01-08 13:23:28','2025-01-08 13:23:28'),(130,16,49,'content creation',50,'2025-01-08 13:23:28','2025-01-08 13:23:28'),(131,16,50,'Preparing budgets',30,'2025-01-08 13:23:28','2025-01-08 13:23:28'),(132,16,50,'account payable/receivable',25,'2025-01-08 13:23:28','2025-01-08 13:23:28'),(133,16,50,'Oversee tax',15,'2025-01-08 13:23:28','2025-01-08 13:23:28'),(134,16,50,'Identify cost saving',30,'2025-01-08 13:23:28','2025-01-08 13:23:28'),(135,16,51,'Recruite and onboard employees',30,'2025-01-08 13:23:28','2025-01-08 13:23:28'),(136,16,51,'payroll management',30,'2025-01-08 13:23:28','2025-01-08 13:23:28'),(137,16,51,'workspace management',30,'2025-01-08 13:23:28','2025-01-08 13:23:28'),(138,16,51,'train employees',10,'2025-01-08 13:23:28','2025-01-08 13:23:28'),(139,16,52,'Identify and qaulify leads',20,'2025-01-08 13:23:28','2025-01-08 13:23:28'),(140,16,52,'develop proposals',50,'2025-01-08 13:23:28','2025-01-08 13:23:28'),(141,16,52,'colaborate witth sales and marketing teams',30,'2025-01-08 13:23:28','2025-01-08 13:23:28'),(166,18,62,'machine learning',20,'2025-01-09 04:33:08','2025-01-09 04:33:08'),(167,18,62,'data pipeline',30,'2025-01-09 04:33:08','2025-01-09 04:33:08'),(168,18,62,'Data flow',40,'2025-01-09 04:33:08','2025-01-09 04:33:08'),(169,18,62,'pyspark',3,'2025-01-09 04:33:08','2025-01-09 04:33:08'),(170,18,62,'Data analytics',7,'2025-01-09 04:33:08','2025-01-09 04:33:08'),(171,18,63,'genAI',40,'2025-01-09 04:33:08','2025-01-09 04:33:08'),(172,18,63,'Transformers',30,'2025-01-09 04:33:08','2025-01-09 04:33:08'),(173,18,63,'NLP',15,'2025-01-09 04:33:08','2025-01-09 04:33:08'),(174,18,63,'Deep learning',15,'2025-01-09 04:33:08','2025-01-09 04:33:08'),(175,10,64,'html',20,'2025-01-09 04:39:48','2025-01-09 04:39:48'),(176,10,64,'api integrations',20,'2025-01-09 04:39:48','2025-01-09 04:39:48'),(177,10,64,'hooks',37,'2025-01-09 04:39:48','2025-01-09 04:39:48'),(178,10,64,'css',23,'2025-01-09 04:39:48','2025-01-09 04:39:48'),(179,10,65,'database',34,'2025-01-09 04:39:48','2025-01-09 04:39:48'),(180,10,65,'apis',23,'2025-01-09 04:39:48','2025-01-09 04:39:48'),(181,10,65,'testing',26,'2025-01-09 04:39:48','2025-01-09 04:39:48'),(182,10,65,'deploy',17,'2025-01-09 04:39:48','2025-01-09 04:39:48');
/*!40000 ALTER TABLE `critical_activities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `email_queue`
--

DROP TABLE IF EXISTS `email_queue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `email_queue` (
  `id` int NOT NULL AUTO_INCREMENT,
  `recipient_id` int NOT NULL,
  `recipient_type` varchar(100) NOT NULL,
  `subject` varchar(100) NOT NULL,
  `body` text NOT NULL,
  `status` varchar(100) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `sent_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_email_queue_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `email_queue`
--

LOCK TABLES `email_queue` WRITE;
/*!40000 ALTER TABLE `email_queue` DISABLE KEYS */;
INSERT INTO `email_queue` VALUES (1,2,'user','Your Login Information and New Report Created','We are excited to have you on board! Below are your login details for accessing the platform.\n  \n            **Login Instructions:**\n            1. Visit the login page: [Insert URL to login page]\n            2. Enter your login credentials:\n               - Email: {recipientEmail}\n               - Password: {recipientPassword}\n               - Role: {role}\n            3. Click on the \"Login\" button to access your account.\n  \n            Additionally, your latest report has been created successfully. Please find the attachment.\n  \n            If you encounter any issues or need further assistance, feel free to contact our support team.\n  \n            Thank you, and we look forward to your participation!\n  \n            Best regards,','sent','2025-01-08 07:11:25','2025-01-08 07:11:36'),(2,2,'user','Your Login Information and New Report Created','We are excited to have you on board! Below are your login details for accessing the platform.\n  \n            **Login Instructions:**\n            1. Visit the login page: [Insert URL to login page]\n            2. Enter your login credentials:\n               - Email: {recipientEmail}\n               - Password: {recipientPassword}\n               - Role: {role}\n            3. Click on the \"Login\" button to access your account.\n  \n            Additionally, your latest report has been created successfully. Please find the attachment.\n  \n            If you encounter any issues or need further assistance, feel free to contact our support team.\n  \n            Thank you, and we look forward to your participation!\n  \n            Best regards,','sent','2025-01-08 07:33:00','2025-01-08 07:33:12'),(3,2,'user','Your Login Information and New Report Created','We are excited to have you on board! Below are your login details for accessing the platform.\n  \n            **Login Instructions:**\n            1. Visit the login page: [Insert URL to login page]\n            2. Enter your login credentials:\n               - Email: {recipientEmail}\n               - Password: {recipientPassword}\n               - Role: {role}\n            3. Click on the \"Login\" button to access your account.\n  \n            Additionally, your latest report has been created successfully. Please find the attachment.\n  \n            If you encounter any issues or need further assistance, feel free to contact our support team.\n  \n            Thank you, and we look forward to your participation!\n  \n            Best regards,','sent','2025-01-08 07:37:08','2025-01-08 07:37:19'),(4,1,'user','Your Login Information and New Report Created','We are excited to have you on board! Below are your login details for accessing the platform.\n  \n            **Login Instructions:**\n            1. Visit the login page: [Insert URL to login page]\n            2. Enter your login credentials:\n               - Email: {recipientEmail}\n               - Password: {recipientPassword}\n               - Role: {role}\n            3. Click on the \"Login\" button to access your account.\n  \n            Additionally, your latest report has been created successfully. Please find the attachment.\n  \n            If you encounter any issues or need further assistance, feel free to contact our support team.\n  \n            Thank you, and we look forward to your participation!\n  \n            Best regards,','sent','2025-01-08 10:08:52','2025-01-08 10:09:03'),(5,1,'user','Your Login Information and New Report Created','We are excited to have you on board! Below are your login details for accessing the platform.\n  \n            **Login Instructions:**\n            1. Visit the login page: [Insert URL to login page]\n            2. Enter your login credentials:\n               - Email: {recipientEmail}\n               - Password: {recipientPassword}\n               - Role: {role}\n            3. Click on the \"Login\" button to access your account.\n  \n            Additionally, your latest report has been created successfully. Please find the attachment.\n  \n            If you encounter any issues or need further assistance, feel free to contact our support team.\n  \n            Thank you, and we look forward to your participation!\n  \n            Best regards,','sent','2025-01-08 10:24:10','2025-01-08 10:24:21'),(6,1,'user','Your Login Information and New Report Created','We are excited to have you on board! Below are your login details for accessing the platform.\n  \n            **Login Instructions:**\n            1. Visit the login page: [Insert URL to login page]\n            2. Enter your login credentials:\n               - Email: {recipientEmail}\n               - Password: {recipientPassword}\n               - Role: {role}\n            3. Click on the \"Login\" button to access your account.\n  \n            Additionally, your latest report has been created successfully. Please find the attachment.\n  \n            If you encounter any issues or need further assistance, feel free to contact our support team.\n  \n            Thank you, and we look forward to your participation!\n  \n            Best regards,','sent','2025-01-08 11:12:31','2025-01-08 11:12:42'),(7,1,'user','Your Login Information and New Report Created','We are excited to have you on board! Below are your login details for accessing the platform.\n  \n            **Login Instructions:**\n            1. Visit the login page: [Insert URL to login page]\n            2. Enter your login credentials:\n               - Email: {recipientEmail}\n               - Password: {recipientPassword}\n               - Role: {role}\n            3. Click on the \"Login\" button to access your account.\n  \n            Additionally, your latest report has been created successfully. Please find the attachment.\n  \n            If you encounter any issues or need further assistance, feel free to contact our support team.\n  \n            Thank you, and we look forward to your participation!\n  \n            Best regards,','sent','2025-01-08 11:22:59','2025-01-08 11:23:10'),(8,6,'user','Your Login Information and New Report Created','We are excited to have you on board! Below are your login details for accessing the platform.\n  \n            **Login Instructions:**\n            1. Visit the login page: [Insert URL to login page]\n            2. Enter your login credentials:\n               - Email: {recipientEmail}\n               - Password: {recipientPassword}\n               - Role: {role}\n            3. Click on the \"Login\" button to access your account.\n  \n            Additionally, your latest report has been created successfully. Please find the attachment.\n  \n            If you encounter any issues or need further assistance, feel free to contact our support team.\n  \n            Thank you, and we look forward to your participation!\n  \n            Best regards,','sent','2025-01-08 12:33:32','2025-01-08 12:33:42'),(9,16,'user','Your Login Information and New Report Created','We are excited to have you on board! Below are your login details for accessing the platform.\n  \n            **Login Instructions:**\n            1. Visit the login page: [Insert URL to login page]\n            2. Enter your login credentials:\n               - Email: {recipientEmail}\n               - Password: {recipientPassword}\n               - Role: {role}\n            3. Click on the \"Login\" button to access your account.\n  \n            Additionally, your latest report has been created successfully. Please find the attachment.\n  \n            If you encounter any issues or need further assistance, feel free to contact our support team.\n  \n            Thank you, and we look forward to your participation!\n  \n            Best regards,','sent','2025-01-08 13:23:43','2025-01-08 13:23:54'),(10,12,'user','Your Login Information and New Report Created','We are excited to have you on board! Below are your login details for accessing the platform.\n  \n            **Login Instructions:**\n            1. Visit the login page: [Insert URL to login page]\n            2. Enter your login credentials:\n               - Email: {recipientEmail}\n               - Password: {recipientPassword}\n               - Role: {role}\n            3. Click on the \"Login\" button to access your account.\n  \n            Additionally, your latest report has been created successfully. Please find the attachment.\n  \n            If you encounter any issues or need further assistance, feel free to contact our support team.\n  \n            Thank you, and we look forward to your participation!\n  \n            Best regards,','sent','2025-01-08 13:28:37','2025-01-08 13:28:48'),(11,12,'user','Your Login Information and New Report Created','We are excited to have you on board! Below are your login details for accessing the platform.\n  \n            **Login Instructions:**\n            1. Visit the login page: [Insert URL to login page]\n            2. Enter your login credentials:\n               - Email: {recipientEmail}\n               - Password: {recipientPassword}\n               - Role: {role}\n            3. Click on the \"Login\" button to access your account.\n  \n            Additionally, your latest report has been created successfully. Please find the attachment.\n  \n            If you encounter any issues or need further assistance, feel free to contact our support team.\n  \n            Thank you, and we look forward to your participation!\n  \n            Best regards,','sent','2025-01-08 13:32:03','2025-01-08 13:32:13'),(12,18,'user','Your Login Information and New Report Created','We are excited to have you on board! Below are your login details for accessing the platform.\n  \n            **Login Instructions:**\n            1. Visit the login page: [Insert URL to login page]\n            2. Enter your login credentials:\n               - Email: {recipientEmail}\n               - Password: {recipientPassword}\n               - Role: {role}\n            3. Click on the \"Login\" button to access your account.\n  \n            Additionally, your latest report has been created successfully. Please find the attachment.\n  \n            If you encounter any issues or need further assistance, feel free to contact our support team.\n  \n            Thank you, and we look forward to your participation!\n  \n            Best regards,','sent','2025-01-08 13:44:37','2025-01-08 13:44:48'),(13,18,'user','Your Login Information and New Report Created','We are excited to have you on board! Below are your login details for accessing the platform.\n  \n            **Login Instructions:**\n            1. Visit the login page: [Insert URL to login page]\n            2. Enter your login credentials:\n               - Email: {recipientEmail}\n               - Password: {recipientPassword}\n               - Role: {role}\n            3. Click on the \"Login\" button to access your account.\n  \n            Additionally, your latest report has been created successfully. Please find the attachment.\n  \n            If you encounter any issues or need further assistance, feel free to contact our support team.\n  \n            Thank you, and we look forward to your participation!\n  \n            Best regards,','sent','2025-01-09 04:28:58','2025-01-09 04:29:09'),(14,18,'user','Your Login Information and New Report Created','We are excited to have you on board! Below are your login details for accessing the platform.\n  \n            **Login Instructions:**\n            1. Visit the login page: [Insert URL to login page]\n            2. Enter your login credentials:\n               - Email: {recipientEmail}\n               - Password: {recipientPassword}\n               - Role: {role}\n            3. Click on the \"Login\" button to access your account.\n  \n            Additionally, your latest report has been created successfully. Please find the attachment.\n  \n            If you encounter any issues or need further assistance, feel free to contact our support team.\n  \n            Thank you, and we look forward to your participation!\n  \n            Best regards,','sent','2025-01-09 04:33:32','2025-01-09 04:33:43'),(15,10,'user','Your Login Information and New Report Created','We are excited to have you on board! Below are your login details for accessing the platform.\n  \n            **Login Instructions:**\n            1. Visit the login page: [Insert URL to login page]\n            2. Enter your login credentials:\n               - Email: {recipientEmail}\n               - Password: {recipientPassword}\n               - Role: {role}\n            3. Click on the \"Login\" button to access your account.\n  \n            Additionally, your latest report has been created successfully. Please find the attachment.\n  \n            If you encounter any issues or need further assistance, feel free to contact our support team.\n  \n            Thank you, and we look forward to your participation!\n  \n            Best regards,','sent','2025-01-09 04:40:17','2025-01-09 04:40:28');
/*!40000 ALTER TABLE `email_queue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `managers`
--

DROP TABLE IF EXISTS `managers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `managers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(50) NOT NULL,
  `dept` varchar(100) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `ix_managers_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `managers`
--

LOCK TABLES `managers` WRITE;
/*!40000 ALTER TABLE `managers` DISABLE KEYS */;
INSERT INTO `managers` VALUES (1,'Manager Test','manager@example.com','string','2025-01-06 11:23:51','2025-01-06 11:23:51'),(2,'manager_new','manager111@example.com',NULL,'2025-01-07 06:30:23','2025-01-07 06:30:23'),(3,'Admin Manager','adminmanager@gmail.com',NULL,'2025-01-08 11:07:35','2025-01-08 11:07:35'),(4,'Jane Smith','jane.smith@example.com','Human Resources','2025-01-08 12:08:33','2025-01-08 12:08:33'),(5,'Alice Johnson','alice.johnson@example.com',NULL,'2025-01-08 12:09:00','2025-01-08 12:09:00'),(6,'Michael Brown','michael.brown@example.com',NULL,'2025-01-08 12:09:12','2025-01-08 12:09:12'),(7,'Emily Davis','emily.davis@example.com','IT','2025-01-08 12:09:41','2025-01-08 12:09:41'),(8,'William Wilson','william.wilson@example.com','Sales','2025-01-08 12:09:57','2025-01-08 12:09:57'),(9,'Sophia Martinez','sophia.martinez@example.com','Customer Support','2025-01-08 12:10:11','2025-01-08 12:10:11'),(10,'James Anderson','james.anderson@example.com','Legal','2025-01-08 12:10:25','2025-01-08 12:10:25'),(11,'Olivia Taylor','olivia.taylor@example.com','R&D','2025-01-08 12:10:42','2025-01-08 12:10:42'),(12,'munil nayak','munil@example.com',NULL,'2025-01-08 12:44:54','2025-01-08 12:44:54'),(13,'heli shah','helishah@gmail.com',NULL,'2025-01-08 12:55:25','2025-01-08 12:55:25'),(14,'srishti','srishti@example.com',NULL,'2025-01-08 13:13:28','2025-01-08 13:13:28'),(15,'Dipa','dipa@example.com',NULL,'2025-01-08 13:38:38','2025-01-08 13:38:38');
/*!40000 ALTER TABLE `managers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `new_notifications`
--

DROP TABLE IF EXISTS `new_notifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `new_notifications` (
  `id` int NOT NULL AUTO_INCREMENT,
  `message` varchar(100) NOT NULL,
  `user_id` int DEFAULT NULL,
  `manager_id` int DEFAULT NULL,
  `is_read` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `manager_id` (`manager_id`),
  KEY `ix_new_notifications_id` (`id`),
  CONSTRAINT `new_notifications_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `new_notifications_ibfk_2` FOREIGN KEY (`manager_id`) REFERENCES `managers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `new_notifications`
--

LOCK TABLES `new_notifications` WRITE;
/*!40000 ALTER TABLE `new_notifications` DISABLE KEYS */;
INSERT INTO `new_notifications` VALUES (1,'root\'s report has been updated to version 3.',NULL,3,1,'2025-01-08 11:12:31'),(2,'root\'s report has been updated to version 4.',NULL,3,1,'2025-01-08 11:22:59'),(3,'root2\'s report has been created successfully.',6,NULL,1,'2025-01-08 12:33:32'),(4,'root7\'s report has been created successfully.',16,NULL,1,'2025-01-08 13:23:43'),(5,'root6\'s report has been created successfully.',12,NULL,1,'2025-01-08 13:28:37'),(6,'root6\'s report has been updated to version 2.',NULL,12,1,'2025-01-08 13:32:03'),(7,'Hitik\'s report has been created successfully.',18,NULL,1,'2025-01-08 13:44:37'),(8,'Hitik\'s report has been updated to version 2.',NULL,15,1,'2025-01-09 04:28:58'),(9,'Manager updated Hitik\'s report to version 3.',18,NULL,1,'2025-01-09 04:33:32'),(10,'root5\'s report has been created successfully.',NULL,15,1,'2025-01-09 04:40:17');
/*!40000 ALTER TABLE `new_notifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `organizations`
--

DROP TABLE IF EXISTS `organizations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `organizations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `ix_organizations_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `organizations`
--

LOCK TABLES `organizations` WRITE;
/*!40000 ALTER TABLE `organizations` DISABLE KEYS */;
INSERT INTO `organizations` VALUES (1,'Dummy','2025-01-06 11:24:03','2025-01-06 11:24:03'),(2,'Global Finance Corp','2025-01-08 12:11:31','2025-01-08 12:11:31'),(3,'PeopleFirst Solutions','2025-01-08 12:11:45','2025-01-08 12:11:45'),(4,'BrightPath Marketing','2025-01-08 12:11:57','2025-01-08 12:11:57'),(5,'TechPioneers Ltd','2025-01-08 12:12:11','2025-01-08 12:12:11'),(6,'NextGen Sales Group','2025-01-08 12:12:26','2025-01-08 12:12:26'),(7,'CareHub Solutions','2025-01-08 12:12:38','2025-01-08 12:12:38'),(8,'LexPro Legal Advisors','2025-01-08 12:12:47','2025-01-08 12:12:47'),(9,'SupplyLink Enterprises','2025-01-08 12:13:00','2025-01-08 12:13:00');
/*!40000 ALTER TABLE `organizations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report_contents`
--

DROP TABLE IF EXISTS `report_contents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report_contents` (
  `id` int NOT NULL AUTO_INCREMENT,
  `report_version_id` int NOT NULL,
  `content` text NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `report_version_id` (`report_version_id`),
  KEY `ix_report_contents_id` (`id`),
  CONSTRAINT `report_contents_ibfk_1` FOREIGN KEY (`report_version_id`) REFERENCES `report_versions` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report_contents`
--

LOCK TABLES `report_contents` WRITE;
/*!40000 ALTER TABLE `report_contents` DISABLE KEYS */;
INSERT INTO `report_contents` VALUES (1,1,'{}','2025-01-07 12:58:03','2025-01-07 12:58:03'),(2,2,'{}','2025-01-08 05:10:50','2025-01-08 05:10:50'),(3,3,'{}','2025-01-08 06:24:39','2025-01-08 06:24:39'),(4,4,'{}','2025-01-08 06:33:13','2025-01-08 06:33:13'),(5,5,'{\"role_review\": {\"name\": \"root1\", \"purpose\": \"survey\", \"title\": \"software engineer\", \"organization\": \"xyz\", \"date\": \"2025-01-08\", \"prepared_by\": \"xyz\", \"job_summary\": \"string string string string string\"}, \"core_focus_areas\": [{\"area\": \"frontend\", \"time_spent\": 50.0, \"importance\": 50.0, \"critical_activities\": [{\"area\": \"html\", \"importance\": 30.0}, {\"area\": \"api integrations\", \"importance\": 40.0}, {\"area\": \"js\", \"importance\": 30.0}]}, {\"area\": \"backend\", \"time_spent\": 50.0, \"importance\": 50.0, \"critical_activities\": [{\"area\": \"database\", \"importance\": 30.0}, {\"area\": \"apis\", \"importance\": 60.0}, {\"area\": \"testing\", \"importance\": 10.0}]}]}','2025-01-08 06:52:02','2025-01-08 06:52:02'),(6,6,'{\"role_review\": {\"name\": \"root1\", \"purpose\": \"survey\", \"title\": \"software engineer\", \"organization\": \"xyz\", \"date\": \"2025-01-08\", \"prepared_by\": \"xyz\", \"job_summary\": \"string string string string string\"}, \"core_focus_areas\": [{\"area\": \"frontend\", \"time_spent\": 50.0, \"importance\": 50.0, \"critical_activities\": [{\"area\": \"html\", \"importance\": 20.0}, {\"area\": \"api integrations\", \"importance\": 50.0}, {\"area\": \"js\", \"importance\": 30.0}]}, {\"area\": \"backend\", \"time_spent\": 50.0, \"importance\": 50.0, \"critical_activities\": [{\"area\": \"database\", \"importance\": 30.0}, {\"area\": \"apis\", \"importance\": 60.0}, {\"area\": \"testing\", \"importance\": 10.0}]}]}','2025-01-08 07:11:24','2025-01-08 07:11:24'),(7,7,'{\"role_review\": {\"name\": \"root1\", \"purpose\": \"survey\", \"title\": \"software engineer\", \"organization\": \"xyz\", \"date\": \"2025-01-08\", \"prepared_by\": \"xyz\", \"job_summary\": \"string string string string string\"}, \"core_focus_areas\": [{\"area\": \"frontend\", \"time_spent\": 50.0, \"importance\": 50.0, \"critical_activities\": [{\"area\": \"html\", \"importance\": 35.0}, {\"area\": \"api integrations\", \"importance\": 35.0}, {\"area\": \"js\", \"importance\": 30.0}]}, {\"area\": \"backend\", \"time_spent\": 50.0, \"importance\": 50.0, \"critical_activities\": [{\"area\": \"database\", \"importance\": 40.0}, {\"area\": \"apis\", \"importance\": 40.0}, {\"area\": \"testing\", \"importance\": 20.0}]}]}','2025-01-08 07:32:59','2025-01-08 07:32:59'),(8,8,'{\"role_review\": {\"name\": \"root1\", \"purpose\": \"survey\", \"title\": \"software engineer\", \"organization\": \"xyz\", \"date\": \"2025-01-08\", \"prepared_by\": \"xyz\", \"job_summary\": \"string string string string string\"}, \"core_focus_areas\": [{\"area\": \"frontend\", \"time_spent\": 50.0, \"importance\": 50.0, \"critical_activities\": [{\"area\": \"www\", \"importance\": 100.0}]}, {\"area\": \"backend\", \"time_spent\": 50.0, \"importance\": 50.0, \"critical_activities\": [{\"area\": \"www2\", \"importance\": 100.0}]}]}','2025-01-08 07:37:08','2025-01-08 07:37:08'),(9,9,'{\"role_review\": {\"name\": \"root\", \"purpose\": \"survey\", \"title\": \"software engineer\", \"organization\": \"xyzzy\", \"date\": \"2025-01-08\", \"prepared_by\": \"xyzzy\", \"job_summary\": \"A Software Engineer is responsible for designing, developing, testing, and maintaining software applications and systems.\"}, \"core_focus_areas\": [{\"area\": \"frontend\", \"time_spent\": 50.0, \"importance\": 50.0, \"critical_activities\": [{\"area\": \"html\", \"importance\": 30.0}, {\"area\": \"api integrations\", \"importance\": 40.0}, {\"area\": \"design\", \"importance\": 30.0}]}, {\"area\": \"backend\", \"time_spent\": 40.0, \"importance\": 30.0, \"critical_activities\": [{\"area\": \"database\", \"importance\": 35.0}, {\"area\": \"apis\", \"importance\": 45.0}, {\"area\": \"testing\", \"importance\": 20.0}]}, {\"area\": \"deployment\", \"time_spent\": 10.0, \"importance\": 20.0, \"critical_activities\": [{\"area\": \"aws setup\", \"importance\": 50.0}, {\"area\": \"nginx\", \"importance\": 50.0}]}]}','2025-01-08 10:08:52','2025-01-08 10:08:52'),(10,10,'{\"role_review\": {\"name\": \"root\", \"purpose\": \"survey\", \"title\": \"software engineer\", \"organization\": \"xyzzy\", \"date\": \"2025-01-08\", \"prepared_by\": \"xyzzy\", \"job_summary\": \"A Software Engineer is responsible for designing, developing, testing, and maintaining software applications and systems.\"}, \"core_focus_areas\": [{\"area\": \"frontend\", \"time_spent\": 100.0, \"importance\": 100.0, \"critical_activities\": [{\"area\": \"test\", \"importance\": 100.0}]}]}','2025-01-08 10:24:09','2025-01-08 10:24:09'),(11,11,'{\"role_review\": {\"name\": \"root\", \"purpose\": \"survey\", \"title\": \"software engineer\", \"organization\": \"xyzzy\", \"date\": \"2025-01-08\", \"prepared_by\": \"xyz\", \"job_summary\": \"A Software Engineer is responsible for designing, developing, testing, and maintaining software applications and systems.\"}, \"core_focus_areas\": [{\"area\": \"frontend\", \"time_spent\": 30.0, \"importance\": 40.0, \"critical_activities\": [{\"area\": \"html\", \"importance\": 30.0}, {\"area\": \"api integrations\", \"importance\": 30.0}, {\"area\": \"js\", \"importance\": 40.0}]}, {\"area\": \"backend\", \"time_spent\": 40.0, \"importance\": 50.0, \"critical_activities\": [{\"area\": \"database\", \"importance\": 40.0}, {\"area\": \"apis\", \"importance\": 50.0}, {\"area\": \"testing\", \"importance\": 10.0}]}, {\"area\": \"deployment\", \"time_spent\": 30.0, \"importance\": 10.0, \"critical_activities\": [{\"area\": \"aws setup\", \"importance\": 50.0}, {\"area\": \"nginx\", \"importance\": 30.0}, {\"area\": \"cors\", \"importance\": 20.0}]}]}','2025-01-08 11:12:31','2025-01-08 11:12:31'),(12,12,'{\"role_review\": {\"name\": \"root\", \"purpose\": \"survey\", \"title\": \"software engineer\", \"organization\": \"xyz\", \"date\": \"2025-01-08\", \"prepared_by\": \"xyz\", \"job_summary\": \"A Software Engineer is responsible for designing, developing, testing, and maintaining software applications and systems.\"}, \"core_focus_areas\": [{\"area\": \"frontend\", \"time_spent\": 30.0, \"importance\": 40.0, \"critical_activities\": [{\"area\": \"html\", \"importance\": 20.0}, {\"area\": \"api integrations\", \"importance\": 30.0}, {\"area\": \"js\", \"importance\": 30.0}, {\"area\": \"design\", \"importance\": 20.0}]}, {\"area\": \"backend\", \"time_spent\": 40.0, \"importance\": 50.0, \"critical_activities\": [{\"area\": \"database\", \"importance\": 30.0}, {\"area\": \"apis\", \"importance\": 30.0}, {\"area\": \"pdf generation apis\", \"importance\": 40.0}]}, {\"area\": \"testing\", \"time_spent\": 10.0, \"importance\": 5.0, \"critical_activities\": [{\"area\": \"unit testing\", \"importance\": 50.0}, {\"area\": \"program testing\", \"importance\": 30.0}, {\"area\": \"git workflow\", \"importance\": 20.0}]}, {\"area\": \"deployment\", \"time_spent\": 20.0, \"importance\": 5.0, \"critical_activities\": [{\"area\": \"aws setup\", \"importance\": 30.0}, {\"area\": \"s3 buckets\", \"importance\": 30.0}, {\"area\": \"nginx\", \"importance\": 20.0}, {\"area\": \"ec2\", \"importance\": 20.0}]}]}','2025-01-08 11:22:59','2025-01-08 11:22:59'),(13,13,'{\"role_review\": {\"name\": \"root2\", \"purpose\": \"survey\", \"title\": \"senior software engineer\", \"organization\": \"Finance\", \"date\": \"2024-12-28\", \"prepared_by\": \"xyz\", \"job_summary\": \"i worked in frontend and backend\"}, \"core_focus_areas\": [{\"area\": \"frontend\", \"time_spent\": 40.0, \"importance\": 50.0, \"critical_activities\": [{\"area\": \"html\", \"importance\": 30.0}, {\"area\": \"api integrations\", \"importance\": 30.0}, {\"area\": \"js\", \"importance\": 40.0}]}, {\"area\": \"backend\", \"time_spent\": 60.0, \"importance\": 50.0, \"critical_activities\": [{\"area\": \"database\", \"importance\": 30.0}, {\"area\": \"apis\", \"importance\": 30.0}, {\"area\": \"testing\", \"importance\": 30.0}]}]}','2025-01-08 12:33:31','2025-01-08 12:33:31'),(14,14,'{\"role_review\": {\"name\": \"root7\", \"purpose\": \"survey\", \"title\": \"senior software engineer\", \"organization\": \"IT Idol\", \"date\": \"2025-01-04\", \"prepared_by\": \"xyz\", \"job_summary\": \"Software Development: Design, develop, and test software applications based on project requirements.\"}, \"core_focus_areas\": [{\"area\": \"Marketing\", \"time_spent\": 20.0, \"importance\": 30.0, \"critical_activities\": [{\"area\": \"SEO optimization\", \"importance\": 30.0}, {\"area\": \"digital marketing\", \"importance\": 20.0}, {\"area\": \"content creation\", \"importance\": 50.0}]}, {\"area\": \"Finance\", \"time_spent\": 30.0, \"importance\": 30.0, \"critical_activities\": [{\"area\": \"Preparing budgets\", \"importance\": 30.0}, {\"area\": \"account payable/receivable\", \"importance\": 25.0}, {\"area\": \"Oversee tax\", \"importance\": 15.0}, {\"area\": \"Identify cost saving\", \"importance\": 30.0}]}, {\"area\": \"HR\", \"time_spent\": 30.0, \"importance\": 25.0, \"critical_activities\": [{\"area\": \"Recruite and onboard employees\", \"importance\": 30.0}, {\"area\": \"payroll management\", \"importance\": 30.0}, {\"area\": \"workspace management\", \"importance\": 30.0}, {\"area\": \"train employees\", \"importance\": 10.0}]}, {\"area\": \"BDE\", \"time_spent\": 20.0, \"importance\": 15.0, \"critical_activities\": [{\"area\": \"Identify and qaulify leads\", \"importance\": 20.0}, {\"area\": \"develop proposals\", \"importance\": 50.0}, {\"area\": \"colaborate witth sales and marketing teams\", \"importance\": 30.0}]}]}','2025-01-08 13:23:43','2025-01-08 13:23:43'),(15,15,'{\"role_review\": {\"name\": \"root6\", \"purpose\": \"survey\", \"title\": \"senior software engineer\", \"organization\": \"IT Idol\", \"date\": \"2025-01-08\", \"prepared_by\": \"xyz\", \"job_summary\": \"software engineer worked on frontend and backend\"}, \"core_focus_areas\": [{\"area\": \"aaa\", \"time_spent\": 100.0, \"importance\": 100.0, \"critical_activities\": [{\"area\": \"aaa\", \"importance\": 100.0}]}]}','2025-01-08 13:28:37','2025-01-08 13:28:37'),(16,16,'{\"role_review\": {\"name\": \"root6\", \"purpose\": \"survey\", \"title\": \"senior software engineer\", \"organization\": \"IT Idol\", \"date\": \"2025-01-08\", \"prepared_by\": \"xyz\", \"job_summary\": \"software engineer worked on frontend and backend\"}, \"core_focus_areas\": [{\"area\": \"ddd\", \"time_spent\": 100.0, \"importance\": 100.0, \"critical_activities\": [{\"area\": \"ccc\", \"importance\": 100.0}]}]}','2025-01-08 13:32:02','2025-01-08 13:32:02'),(17,17,'{\"role_review\": {\"name\": \"hitik\", \"purpose\": \"survey\", \"title\": \"senior software developer\", \"organization\": \"Technoforce\", \"date\": \"2025-01-04\", \"prepared_by\": \"xyz\", \"job_summary\": \"Software engineer role includes frontend and backend technologies\"}, \"core_focus_areas\": [{\"area\": \"Marketing\", \"time_spent\": 30.0, \"importance\": 20.0, \"critical_activities\": [{\"area\": \"SEO optimization\", \"importance\": 20.0}, {\"area\": \"content creation\", \"importance\": 50.0}, {\"area\": \"digital marketing\", \"importance\": 30.0}]}, {\"area\": \"HR\", \"time_spent\": 30.0, \"importance\": 40.0, \"critical_activities\": [{\"area\": \"Recruites and onborad employees\", \"importance\": 30.0}, {\"area\": \"manage payrolls\", \"importance\": 40.0}, {\"area\": \"workspace management\", \"importance\": 25.0}, {\"area\": \"train employees\", \"importance\": 5.0}]}, {\"area\": \"Finance\", \"time_spent\": 30.0, \"importance\": 20.0, \"critical_activities\": [{\"area\": \"Manage accounts payable/recievable\", \"importance\": 50.0}, {\"area\": \"Focus on cost savings\", \"importance\": 50.0}]}, {\"area\": \"BDE\", \"time_spent\": 10.0, \"importance\": 20.0, \"critical_activities\": [{\"area\": \"Identify and qualify leads\", \"importance\": 40.0}, {\"area\": \"develop proposals\", \"importance\": 30.0}, {\"area\": \"collaborate witj sales and marketting teams\", \"importance\": 30.0}]}]}','2025-01-08 13:44:37','2025-01-08 13:44:37'),(18,18,'{\"role_review\": {\"name\": \"hitik\", \"purpose\": \"survey\", \"title\": \"senior software developer\", \"organization\": \"Technoforce\", \"date\": \"2025-01-09\", \"prepared_by\": \"HR\", \"job_summary\": \"Software engineer role includes frontend and backend technologies\"}, \"core_focus_areas\": [{\"area\": \"frontend\", \"time_spent\": 30.0, \"importance\": 40.0, \"critical_activities\": [{\"area\": \"html\", \"importance\": 25.0}, {\"area\": \"api integrations\", \"importance\": 25.0}, {\"area\": \"js\", \"importance\": 50.0}]}, {\"area\": \"backend\", \"time_spent\": 40.0, \"importance\": 30.0, \"critical_activities\": [{\"area\": \"database\", \"importance\": 30.0}, {\"area\": \"apis\", \"importance\": 30.0}, {\"area\": \"testing\", \"importance\": 40.0}]}, {\"area\": \"deployment\", \"time_spent\": 30.0, \"importance\": 30.0, \"critical_activities\": [{\"area\": \"aws setup\", \"importance\": 25.0}, {\"area\": \"nginx\", \"importance\": 25.0}, {\"area\": \"s3 buckets\", \"importance\": 35.0}, {\"area\": \"git workflow\", \"importance\": 15.0}]}]}','2025-01-09 04:28:58','2025-01-09 04:28:58'),(19,19,'{\"role_review\": {\"name\": \"hitik\", \"purpose\": \"survey\", \"title\": \"senior software developer\", \"organization\": \"Technoforce\", \"date\": \"2025-01-09\", \"prepared_by\": \"HR\", \"job_summary\": \"Software engineer role includes frontend and backend technologies\"}, \"core_focus_areas\": [{\"area\": \"data science\", \"time_spent\": 50.0, \"importance\": 50.0, \"critical_activities\": [{\"area\": \"machine learning\", \"importance\": 20.0}, {\"area\": \"data pipeline\", \"importance\": 30.0}, {\"area\": \"Data flow\", \"importance\": 40.0}, {\"area\": \"pyspark\", \"importance\": 3.0}, {\"area\": \"Data analytics\", \"importance\": 7.0}]}, {\"area\": \"AI\", \"time_spent\": 50.0, \"importance\": 50.0, \"critical_activities\": [{\"area\": \"genAI\", \"importance\": 40.0}, {\"area\": \"Transformers\", \"importance\": 30.0}, {\"area\": \"NLP\", \"importance\": 15.0}, {\"area\": \"Deep learning\", \"importance\": 15.0}]}]}','2025-01-09 04:33:32','2025-01-09 04:33:32'),(20,20,'{\"role_review\": {\"name\": \"root5\", \"purpose\": \"survey\", \"title\": \"senior software developer\", \"organization\": \"berthpath\", \"date\": \"2025-01-11\", \"prepared_by\": \"root5\", \"job_summary\": \"Software Development: Design, develop, and test software applications based on project requirements.\\n\"}, \"core_focus_areas\": [{\"area\": \"frontend\", \"time_spent\": 40.0, \"importance\": 40.0, \"critical_activities\": [{\"area\": \"html\", \"importance\": 20.0}, {\"area\": \"api integrations\", \"importance\": 20.0}, {\"area\": \"hooks\", \"importance\": 37.0}, {\"area\": \"css\", \"importance\": 23.0}]}, {\"area\": \"backend\", \"time_spent\": 60.0, \"importance\": 60.0, \"critical_activities\": [{\"area\": \"database\", \"importance\": 34.0}, {\"area\": \"apis\", \"importance\": 23.0}, {\"area\": \"testing\", \"importance\": 26.0}, {\"area\": \"deploy\", \"importance\": 17.0}]}]}','2025-01-09 04:40:16','2025-01-09 04:40:16');
/*!40000 ALTER TABLE `report_contents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report_versions`
--

DROP TABLE IF EXISTS `report_versions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report_versions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `report_id` int NOT NULL,
  `version_number` int NOT NULL,
  `generated_at` datetime DEFAULT NULL,
  `pdf_path` varchar(100) NOT NULL,
  `manager_comments` text,
  PRIMARY KEY (`id`),
  KEY `ix_report_versions_id` (`id`),
  KEY `report_id` (`report_id`),
  CONSTRAINT `report_versions_ibfk_1` FOREIGN KEY (`report_id`) REFERENCES `reports` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report_versions`
--

LOCK TABLES `report_versions` WRITE;
/*!40000 ALTER TABLE `report_versions` DISABLE KEYS */;
INSERT INTO `report_versions` VALUES (1,1,1,'2025-01-07 12:58:03','./uploads/20250107125803_report_31 (31).pdf',NULL),(2,1,2,'2025-01-08 05:10:50','https://activate-pdfstorage.s3.ap-southeast-2.amazonaws.com/20250108051050_report_41.pdf',NULL),(3,1,3,'2025-01-08 06:24:39','https://activate-pdfstorage.s3.ap-southeast-2.amazonaws.com/20250108062438_report_31 (35).pdf',NULL),(4,1,4,'2025-01-08 06:33:13','https://activate-pdfstorage.s3.ap-southeast-2.amazonaws.com/20250108063312_report_31 (35).pdf',NULL),(5,2,1,'2025-01-08 06:52:02','https://activate-pdfstorage.s3.ap-southeast-2.amazonaws.com/20250108065201_report_31 (35).pdf',NULL),(6,2,2,'2025-01-08 07:11:24','https://activate-pdfstorage.s3.ap-southeast-2.amazonaws.com/20250108071124_report_2.pdf',NULL),(7,2,3,'2025-01-08 07:32:59','https://activate-pdfstorage.s3.ap-southeast-2.amazonaws.com/20250108073259_report_2.pdf',NULL),(8,2,4,'2025-01-08 07:37:08','https://activate-pdfstorage.s3.ap-southeast-2.amazonaws.com/20250108073707_report_2.pdf',NULL),(9,3,1,'2025-01-08 10:08:52','report_1.pdf',NULL),(10,3,2,'2025-01-08 10:24:09','report_1.pdf',NULL),(11,3,3,'2025-01-08 11:12:31','report_1.pdf',NULL),(12,3,4,'2025-01-08 11:22:59','report_1.pdf',NULL),(13,4,1,'2025-01-08 12:33:31','report_6.pdf',NULL),(14,5,1,'2025-01-08 13:23:43','report_16.pdf',NULL),(15,6,1,'2025-01-08 13:28:37','report_12.pdf',NULL),(16,6,2,'2025-01-08 13:32:02','report_12.pdf',NULL),(17,7,1,'2025-01-08 13:44:37','report_18.pdf',NULL),(18,7,2,'2025-01-09 04:28:58','report_18.pdf',NULL),(19,7,3,'2025-01-09 04:33:32','report_18.pdf',NULL),(20,8,1,'2025-01-09 04:40:16','report_10.pdf',NULL);
/*!40000 ALTER TABLE `report_versions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reports`
--

DROP TABLE IF EXISTS `reports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reports` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `manager_id` int NOT NULL,
  `current_version_id` int DEFAULT NULL,
  `pdf_path` varchar(100) NOT NULL,
  `role` varchar(50) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_reports_id` (`id`),
  KEY `current_version_id` (`current_version_id`),
  KEY `manager_id` (`manager_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `reports_ibfk_1` FOREIGN KEY (`current_version_id`) REFERENCES `report_versions` (`id`),
  CONSTRAINT `reports_ibfk_2` FOREIGN KEY (`manager_id`) REFERENCES `managers` (`id`),
  CONSTRAINT `reports_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reports`
--

LOCK TABLES `reports` WRITE;
/*!40000 ALTER TABLE `reports` DISABLE KEYS */;
INSERT INTO `reports` VALUES (1,4,1,4,'./uploads/20250107125803_report_31 (31).pdf','employee','2025-01-07 12:58:03','2025-01-08 06:33:13'),(2,2,1,8,'https://activate-pdfstorage.s3.ap-southeast-2.amazonaws.com/20250108065201_report_31 (35).pdf','employee','2025-01-08 06:52:02','2025-01-08 07:37:08'),(3,1,2,12,'report_1.pdf','employee','2025-01-08 10:08:52','2025-01-08 11:22:59'),(4,6,3,13,'report_6.pdf','employee','2025-01-08 12:33:31','2025-01-08 12:33:31'),(5,16,3,14,'report_16.pdf','employee','2025-01-08 13:23:43','2025-01-08 13:23:43'),(6,12,13,16,'report_12.pdf','employee','2025-01-08 13:28:37','2025-01-08 13:32:02'),(7,18,15,19,'report_18.pdf','employee','2025-01-08 13:44:37','2025-01-09 04:33:32'),(8,10,15,20,'report_10.pdf','employee','2025-01-09 04:40:16','2025-01-09 04:40:16');
/*!40000 ALTER TABLE `reports` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role_review`
--

DROP TABLE IF EXISTS `role_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role_review` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `purpose` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `title` varchar(100) NOT NULL,
  `organization` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `prepared_by` varchar(100) NOT NULL,
  `job_summary` varchar(200) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `role_review_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role_review`
--

LOCK TABLES `role_review` WRITE;
/*!40000 ALTER TABLE `role_review` DISABLE KEYS */;
INSERT INTO `role_review` VALUES (1,1,'survey','root','software engineer','xyz','2025-01-08','xyz','A Software Engineer is responsible for designing, developing, testing, and maintaining software applications and systems.','2025-01-07 04:23:41','2025-01-08 11:34:51'),(2,2,'survey','root1','software engineer','xyz','2025-01-08','xyz','string string string string string','2025-01-07 04:46:29','2025-01-08 07:36:31'),(3,6,'survey','root2','senior software engineer','Finance','2024-12-28','xyz','i worked in frontend and backend','2025-01-08 12:32:47','2025-01-08 12:32:47'),(4,12,'survey','root6','senior software engineer','IT Idol','2025-01-09','xyz','software engineer worked on frontend and backend','2025-01-08 13:00:55','2025-01-09 09:56:14'),(5,16,'survey','root7','senior software engineer','IT Idol','2025-01-04','xyz','Software Development: Design, develop, and test software applications based on project requirements.','2025-01-08 13:19:16','2025-01-08 13:19:16'),(6,18,'survey','hitik','senior software developer','Technoforce','2025-01-09','HR','Software engineer role includes frontend and backend technologies','2025-01-08 13:41:03','2025-01-09 04:29:54'),(7,10,'survey','root5','senior software developer','berthpath','2025-01-11','root5','Software Development: Design, develop, and test software applications based on project requirements.\n','2025-01-09 04:38:20','2025-01-09 04:38:20');
/*!40000 ALTER TABLE `role_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_roles`
--

DROP TABLE IF EXISTS `user_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_roles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `role` varchar(50) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_user_roles_id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_roles`
--

LOCK TABLES `user_roles` WRITE;
/*!40000 ALTER TABLE `user_roles` DISABLE KEYS */;
INSERT INTO `user_roles` VALUES (1,'employee','2025-01-06 10:45:23','2025-01-06 10:45:23'),(2,'manager','2025-01-06 10:45:23','2025-01-06 10:45:23');
/*!40000 ALTER TABLE `user_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(16) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password_hash` varchar(100) NOT NULL,
  `verification_code` varchar(10) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `role_id` int DEFAULT NULL,
  `organization_id` int DEFAULT NULL,
  `job_title` varchar(50) DEFAULT NULL,
  `manager_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `role_id` (`role_id`),
  KEY `organization_id` (`organization_id`),
  KEY `manager_id` (`manager_id`),
  KEY `ix_users_id` (`id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `user_roles` (`id`),
  CONSTRAINT `users_ibfk_2` FOREIGN KEY (`organization_id`) REFERENCES `organizations` (`id`),
  CONSTRAINT `users_ibfk_3` FOREIGN KEY (`manager_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'root','root@example.com','$2b$12$gg3hdw76oLkFWZtR.9ip9uf9SEZdl.sDzgbxhRzXViSfqht9kussq',NULL,'2025-01-06 10:45:23','2025-01-06 10:45:23',1,1,'Senior software engineer',3),(2,'root1','root1@example.com','$2b$12$yzwum4J8BvPYO8tMjJ4VWuB1Zzyoey1Q1KVrQbcoL9Y7djNE9XQTS',NULL,'2025-01-07 04:45:09','2025-01-07 04:45:09',1,1,'software engineer',1),(3,'manager_new','manager111@example.com','$2b$12$yieHeEiONVbYClYzSRpdUOlt/Go3dyLFjp2wPf6qk1KF345jLr9ia',NULL,'2025-01-07 06:30:23','2025-01-07 06:30:23',2,NULL,NULL,NULL),(4,'string','user@example.com','$2b$12$cR27dPLuXLLbImt9.XKLqOyFkAhFF1/geP2HxjfmRfiLvA065lME6',NULL,'2025-01-07 11:47:01','2025-01-07 11:47:01',1,NULL,NULL,NULL),(5,'Admin Manager','adminmanager@gmail.com','$2b$12$.7ObGyetYoiLbjyUetw7U.XUx4xy8kLpQ0c9ZeeWsB6cHOp5NVIY2',NULL,'2025-01-08 11:07:35','2025-01-08 11:07:35',2,NULL,NULL,NULL),(6,'root2','root2@example.com','$2b$12$Qjtkxp67HbgEC3aVBAzo4.o4I4QHUyfOjxLTKqnK/mLssawz7EgNm',NULL,'2025-01-08 11:31:47','2025-01-08 11:31:47',1,5,'Senior software engineer',3),(7,'root3','root3@example.com','$2b$12$3xf5Mak0sUaobMkKMwe0QuAX0ssYic3yf9UMZ31/.K2pef2QVMRZu',NULL,'2025-01-08 12:44:20','2025-01-08 12:44:20',1,NULL,NULL,NULL),(8,'munil nayak','munil@example.com','$2b$12$gGBfFz6FFP7M1RGeRUWt7es8S3Ds.gMnjVXlUcp0GHUAycYTpMRnq',NULL,'2025-01-08 12:44:53','2025-01-08 12:44:53',2,NULL,NULL,NULL),(9,'root4','root4@example.com','$2b$12$57UCKadxwLx4xt7it1ylcehysFghp/KVA25w63AitOtaAVUurlpvO',NULL,'2025-01-08 12:46:56','2025-01-08 12:46:56',1,NULL,NULL,NULL),(10,'root5','root5@example.com','$2b$12$x3sOFe/X7uthgiy0Xf6Xf./7eNnocAYJmStEojCIJ/R9/sc2J59AG',NULL,'2025-01-08 12:52:55','2025-01-08 12:52:55',1,4,'Senior software engineer',15),(11,'heli shah','helishah@gmail.com','$2b$12$W2ZnDnw03nOIYFZkxD.5SuJmc5/zZCEnOzL.cG4YfpDIo5Mt/N1.G',NULL,'2025-01-08 12:55:25','2025-01-08 12:55:25',2,NULL,NULL,NULL),(12,'root6','root6@example.com','$2b$12$JriShBZvMoU.LNFTKPuTXOsgBSDQPjlkJ9a6m0xYTRLwBXY4MOFmK',NULL,'2025-01-08 12:59:03','2025-01-08 12:59:03',1,4,'Senior software engineer',12),(13,'root6','root6@gmail.com','$2b$12$X9qlrheP43poTR9TqyUGZOrSVvbfIRS6tB2Zwcaj4NRkRIwZv3ZCO',NULL,'2025-01-08 13:02:37','2025-01-08 13:02:37',1,NULL,NULL,NULL),(14,'srishti','srishti@example.com','$2b$12$cSS.qJXNRrsMPxtqP5R99.FwCn90uqE/nf9E0LTHPtY0zj7fk4.wm',NULL,'2025-01-08 13:13:28','2025-01-08 13:13:28',2,NULL,NULL,NULL),(15,'tisha','tisha@example.com','$2b$12$1UAnEN.1oLTu0s9a4oW5W./qXKbgSSGVsQ3CecOhIahWUFUOxu/Iq',NULL,'2025-01-08 13:14:32','2025-01-08 13:14:32',1,7,'senior software engineer',14),(16,'root7','root7@example.com','$2b$12$OHTkmCsF5wQDRPdl2rd5S.jtzuZSYlfJyGlMBRw9M.wgOsEDivo9W',NULL,'2025-01-08 13:18:01','2025-01-08 13:18:01',1,4,'Senior software engineer',3),(17,'Dipa','dipa@example.com','$2b$12$x3Kgtb9ZK04KyyVNPvnxEuq6VoSg2wK0W1mlBVFogYCHJHhxiFXvi',NULL,'2025-01-08 13:38:38','2025-01-08 13:38:38',2,NULL,NULL,NULL),(18,'Hitik','hitikshah@example.com','$2b$12$Zf69np9ga.tK2gG9UzUCuOVOSiwIua1lW8cnnMRZa4z8LRzPo7oAi',NULL,'2025-01-08 13:39:28','2025-01-08 13:39:28',1,5,'Senior software engineer',15);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-10 10:27:33
