-- MySQL dump 10.16  Distrib 10.1.41-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: E_Commerce
-- ------------------------------------------------------
-- Server version	10.1.41-MariaDB-0+deb9u1

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
-- Table structure for table `Keranjang`
--

DROP TABLE IF EXISTS `Keranjang`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Keranjang` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `total_harga` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `Keranjang_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Keranjang`
--

LOCK TABLES `Keranjang` WRITE;
/*!40000 ALTER TABLE `Keranjang` DISABLE KEYS */;
INSERT INTO `Keranjang` VALUES (1,1,0),(2,2,0);
/*!40000 ALTER TABLE `Keranjang` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `KeranjangDetails`
--

DROP TABLE IF EXISTS `KeranjangDetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `KeranjangDetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `keranjang_id` int(11) NOT NULL,
  `produk_id` int(11) NOT NULL,
  `kuantitas` int(11) NOT NULL,
  `harga` int(11) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `keranjang_id` (`keranjang_id`),
  KEY `produk_id` (`produk_id`),
  CONSTRAINT `KeranjangDetails_ibfk_1` FOREIGN KEY (`keranjang_id`) REFERENCES `Keranjang` (`id`),
  CONSTRAINT `KeranjangDetails_ibfk_2` FOREIGN KEY (`produk_id`) REFERENCES `Produk` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `KeranjangDetails`
--

LOCK TABLES `KeranjangDetails` WRITE;
/*!40000 ALTER TABLE `KeranjangDetails` DISABLE KEYS */;
/*!40000 ALTER TABLE `KeranjangDetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Produk`
--

DROP TABLE IF EXISTS `Produk`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Produk` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nama_produk` varchar(1000) NOT NULL,
  `foto_produk` varchar(1000) NOT NULL,
  `kategori` varchar(255) NOT NULL,
  `harga` int(11) NOT NULL,
  `stok` int(11) NOT NULL,
  `deskripsi` varchar(2000) DEFAULT NULL,
  `jumlah_terjual` int(11) NOT NULL,
  `rating` int(11) NOT NULL,
  `lokasi` varchar(255) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Produk`
--

LOCK TABLES `Produk` WRITE;
/*!40000 ALTER TABLE `Produk` DISABLE KEYS */;
/*!40000 ALTER TABLE `Produk` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Transaksi`
--

DROP TABLE IF EXISTS `Transaksi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Transaksi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `nama_penerima` varchar(255) NOT NULL,
  `no_hp_penerima` varchar(20) NOT NULL,
  `alamat_pengiriman` varchar(1000) NOT NULL,
  `metode_pembayaran` varchar(255) NOT NULL,
  `jasa_kirim` varchar(255) NOT NULL,
  `harga` int(11) NOT NULL,
  `ongkos_kirim` int(11) NOT NULL,
  `diskon` int(11) NOT NULL,
  `total_harga` int(11) NOT NULL,
  `status` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `Transaksi_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Transaksi`
--

LOCK TABLES `Transaksi` WRITE;
/*!40000 ALTER TABLE `Transaksi` DISABLE KEYS */;
/*!40000 ALTER TABLE `Transaksi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TransaksiDetails`
--

DROP TABLE IF EXISTS `TransaksiDetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TransaksiDetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `transaksi_id` int(11) NOT NULL,
  `produk_id` int(11) NOT NULL,
  `kuantitas` int(11) NOT NULL,
  `harga` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `transaksi_id` (`transaksi_id`),
  KEY `produk_id` (`produk_id`),
  CONSTRAINT `TransaksiDetails_ibfk_1` FOREIGN KEY (`transaksi_id`) REFERENCES `Transaksi` (`id`),
  CONSTRAINT `TransaksiDetails_ibfk_2` FOREIGN KEY (`produk_id`) REFERENCES `Produk` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TransaksiDetails`
--

LOCK TABLES `TransaksiDetails` WRITE;
/*!40000 ALTER TABLE `TransaksiDetails` DISABLE KEYS */;
/*!40000 ALTER TABLE `TransaksiDetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserDetails`
--

DROP TABLE IF EXISTS `UserDetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `UserDetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `nama` varchar(255) DEFAULT NULL,
  `alamat` varchar(1000) DEFAULT NULL,
  `no_hp` varchar(20) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `tanggal_lahir` date DEFAULT NULL,
  `foto_profil` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `UserDetails_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserDetails`
--

LOCK TABLES `UserDetails` WRITE;
/*!40000 ALTER TABLE `UserDetails` DISABLE KEYS */;
INSERT INTO `UserDetails` VALUES (1,1,NULL,NULL,NULL,'halo@gmail.com',NULL,NULL),(2,2,NULL,NULL,NULL,'halo2@gmail.com',NULL,NULL);
/*!40000 ALTER TABLE `UserDetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `email` varchar(180) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (1,'ulfah1','halo@gmail.com','7c6a180b36896a0a8c02787eeafb0e4c'),(2,'ulfah2','halo2@gmail.com','7c6a180b36896a0a8c02787eeafb0e4c');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Wishlist`
--

DROP TABLE IF EXISTS `Wishlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Wishlist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `produk_id` int(11) NOT NULL,
  `deleted` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `produk_id` (`produk_id`),
  CONSTRAINT `Wishlist_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`),
  CONSTRAINT `Wishlist_ibfk_2` FOREIGN KEY (`produk_id`) REFERENCES `Produk` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Wishlist`
--

LOCK TABLES `Wishlist` WRITE;
/*!40000 ALTER TABLE `Wishlist` DISABLE KEYS */;
/*!40000 ALTER TABLE `Wishlist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-20 19:57:36
