-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: review
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `rev_id` int NOT NULL,
  `usr_name` varchar(30) DEFAULT NULL,
  `Place` varchar(50) DEFAULT NULL,
  `Reviews` varchar(500) DEFAULT NULL,
  `revdate` date DEFAULT (curdate()),
  `trvl_avl` varchar(50) DEFAULT 'Data not available',
  PRIMARY KEY (`rev_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (1001,'Anonymous123','Calicut','Calicut is definitely worth visiting. When Zamorins ruled, Calicut was the capital of Malabar in northern Kerala. One should not miss out on the many tourist attractions that this destination offers. Moreover, this is the place where most of the spices are produced so this place is worth seeing at least once.','2018-02-01','Night curfews, Sunday complete lockdowns'),(1002,'DB_Admin','Munnar','Munnar is a place you should not miss, the beauty of the place wins the heart of everyone... Tea Museum/plantation & Mattupetty Dam was our highlight... 3-days spends in Munnar was such a great experience... Nice-tour!','2018-04-15','Data not available'),(1003,'Rohit','Cochin','','2019-05-16','Data not available'),(1004,'n','Kannur','','2019-06-05','Data not available'),(1005,'MohanLal','alappuzha','Alappuzha, famous for its boat races, beaches, marine products and coir industry, is a world renowned backwater tourist destination of India. Kuttanad, Alappuzha backwaters and Alappuzha beach are the must-see tourist attractions in the district.','2020-06-08','Data not available'),(1006,'Amrutha','Kasargod ','Good place','2020-08-21','Data not available'),(1007,'Mr.X','Thiruvananthapuram','Good place , with a lot of beaches worth going and not to be missed and a very good hill station 100% recommended','2018-11-21','Data not available'),(1008,'admin','test','test_review','2019-02-22','Data not available'),(1009,'Kiran Kishore','Thrissur','The best time to visit Thrissur is during thrissur pooram in the months of April or May.The festivities are indeed a pleasure for the eyes!','2020-05-30','Data not available'),(1010,'Parvathy P','Kochi','The main attraction for me in Kochi was Wonderla Amusement Park.People vsiting Kochi and having a day to spare should definitely not miss this.Also all pizza lovers ,try out P60Pizzeria in Panampilly Nagar','2019-06-14','Data not available'),(1011,'Klaus M','Wayanad','Best place for a getaway trip!Banasura Sagar Dam and Edakkal Caves should be on your must visit places list!','2018-08-09','Data not available'),(1012,'Elijah M','Idukki','As a person who enjoys trekking,I loved the trekking in Kolukkumalai and the sunrise view point is absolutely amazing!','2020-10-13','Data not available'),(1013,'Joshua ','Kozhikode','My favourite places in kozhikode has been Kappad Beach and Tali temple which worships Lord Shiva.The beach with its winds and everything was a blissful experiece.Tali temple being the oldest and sacred temple in Kerala,i loved its architeture and the amazing wall paintings','2020-12-16','Data not available'),(1014,'Agasthya N','Thrissur','','2018-09-09','Data not available'),(1015,'Kerala_rider','Kerala','Best place ever! God\'s own country!','2021-01-01','Data not available');
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-05 14:05:38
