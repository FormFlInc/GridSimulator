-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 11, 2020 at 02:16 PM
-- Server version: 5.7.26
-- PHP Version: 7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `poo_elec`
--

-- --------------------------------------------------------

--
-- Table structure for table `pe_node`
--

DROP TABLE IF EXISTS `pe_node`;
CREATE TABLE IF NOT EXISTS `pe_node` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `id_sim` int(10) UNSIGNED NOT NULL,
  `id_type` int(10) UNSIGNED NOT NULL,
  `label` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `node_sim` (`id_sim`),
  KEY `node_type` (`id_type`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `pe_node`
--

INSERT INTO `pe_node` (`id`, `id_sim`, `id_type`, `label`) VALUES
(26, 5, 0, 'N1'),
(27, 5, 19, 'N1 40MW'),
(28, 5, 20, 'Pw 10MW'),
(29, 5, 21, 'Ps 10MW'),
(30, 5, 0, 'N2'),
(31, 5, 22, 'Arlon (15MW)');

-- --------------------------------------------------------

--
-- Table structure for table `pe_node_children`
--

DROP TABLE IF EXISTS `pe_node_children`;
CREATE TABLE IF NOT EXISTS `pe_node_children` (
  `id_parent` int(10) UNSIGNED NOT NULL,
  `id_child` int(10) UNSIGNED NOT NULL,
  `max_pwr` int(11) NOT NULL,
  PRIMARY KEY (`id_parent`,`id_child`),
  KEY `node_child` (`id_child`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `pe_node_children`
--

INSERT INTO `pe_node_children` (`id_parent`, `id_child`, `max_pwr`) VALUES
(26, 27, 40),
(26, 28, 10),
(26, 29, 10),
(26, 30, 150),
(30, 31, 15);

-- --------------------------------------------------------

--
-- Table structure for table `pe_sim`
--

DROP TABLE IF EXISTS `pe_sim`;
CREATE TABLE IF NOT EXISTS `pe_sim` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `psw` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `pe_sim`
--

INSERT INTO `pe_sim` (`id`, `name`, `psw`) VALUES
(5, 'sim', 'eb47a13b5ed5bc920b3a4ce65ed6e2c4');

-- --------------------------------------------------------

--
-- Table structure for table `pe_type_meta_field`
--

DROP TABLE IF EXISTS `pe_type_meta_field`;
CREATE TABLE IF NOT EXISTS `pe_type_meta_field` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(30) NOT NULL,
  `simple_type` varchar(1) NOT NULL,
  `label` varchar(30) NOT NULL,
  `field` text NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `node_type_meta` (`type`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `pe_type_meta_field`
--

INSERT INTO `pe_type_meta_field` (`id`, `type`, `simple_type`, `label`, `field`) VALUES
(1, 'prd_gaz', 'p', 'Gaz powerplant', '[\r\n  [\"cost\",10],\r\n  [\"co2\",10],\r\n  [\"power\",10]\r\n]'),
(2, 'prd_nuck', 'p', 'Nucklear powerplant', '[\r\n  [\"cost\",10],\r\n  [\"power\",10],\r\n  [\"t1\",10],\r\n  [\"t2\",10]\r\n]'),
(3, 'prd_wind', 'p', 'Wind turbine', '[\r\n  [\"cost\",10],\r\n  [\"power\",10],\r\n  [\"eff\",10]\r\n]'),
(4, 'prd_sun', 'p', 'Solar panel', '[\r\n  [\"cost\",10],\r\n  [\"power\",10],\r\n  [\"eff\",10]\r\n]'),
(5, 'prd_buy', 'p', 'Buy liason', '[[\"cost\",10]]'),
(6, 'cns_town', 'c', 'Town', '[\r\n  [\"cost\",10],\r\n  [\"power\",10]\r\n]'),
(7, 'cns_enter', 'c', 'Enterprise', '[\r\n  [\"cost\",10],\r\n  [\"power\",10]\r\n]'),
(8, 'cns_diss', 'c', 'Dissipator', '[\r\n  [\"cost\",10],\r\n  [\"power\",10]\r\n]'),
(9, 'cns_sale', 'c', 'Sale liason', '[[\"cost\",10]]');

-- --------------------------------------------------------

--
-- Table structure for table `pe_type_node`
--

DROP TABLE IF EXISTS `pe_type_node`;
CREATE TABLE IF NOT EXISTS `pe_type_node` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `label` varchar(30) DEFAULT NULL,
  `id_sim` int(10) UNSIGNED DEFAULT NULL,
  `type_simple` char(1) NOT NULL,
  `type` varchar(16) DEFAULT NULL,
  `meta` text,
  PRIMARY KEY (`id`),
  KEY `typeNode_sim` (`id_sim`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

--
-- Dumping data for table `pe_type_node`
--

INSERT INTO `pe_type_node` (`id`, `label`, `id_sim`, `type_simple`, `type`, `meta`) VALUES
(0, 'node', NULL, 'n', 'n', NULL),
(19, 'Nuck', 5, 'p', 'prd_nuck', '{\"cost\":\"10\",\"power\":\"40\",\"t1\":\"120\",\"t2\":\"80\"}'),
(20, 'Wind 10MW', 5, 'p', 'prd_wind', '{\"cost\":\"125\",\"power\":\"10\",\"eff\":\"90\"}'),
(21, 'Solar 10MW', 5, 'p', 'prd_sun', '{\"cost\":\"152\",\"power\":\"10\",\"eff\":\"40\"}'),
(22, 'Small town 15MW', 5, 'c', 'cns_town', '{\"cost\":\"10\",\"power\":\"15\"}');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `pe_node`
--
ALTER TABLE `pe_node`
  ADD CONSTRAINT `node_sim` FOREIGN KEY (`id_sim`) REFERENCES `pe_sim` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `node_type` FOREIGN KEY (`id_type`) REFERENCES `pe_type_node` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `pe_node_children`
--
ALTER TABLE `pe_node_children`
  ADD CONSTRAINT `node_child` FOREIGN KEY (`id_child`) REFERENCES `pe_node` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `node_parent` FOREIGN KEY (`id_parent`) REFERENCES `pe_node` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `pe_type_node`
--
ALTER TABLE `pe_type_node`
  ADD CONSTRAINT `typeNode_sim` FOREIGN KEY (`id_sim`) REFERENCES `pe_sim` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;