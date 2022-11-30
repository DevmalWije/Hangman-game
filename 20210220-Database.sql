-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 13, 2021 at 04:16 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hangman_records`
--
CREATE DATABASE IF NOT EXISTS `hangman_records` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `hangman_records`;

-- --------------------------------------------------------

--
-- Table structure for table `final_results`
--

CREATE TABLE `final_results` (
  `Player_name` varchar(20) DEFAULT NULL,
  `Games_won` int(10) DEFAULT NULL,
  `Games_lost` int(20) DEFAULT NULL,
  `Games_played` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `final_results`
--

INSERT INTO `final_results` (`Player_name`, `Games_won`, `Games_lost`, `Games_played`) VALUES
('Kavina', 2, 1, 3),
('Devmal', 4, 4, 8);

-- --------------------------------------------------------

--
-- Table structure for table `game_results`
--

CREATE TABLE `game_results` (
  `Game_No` int(20) DEFAULT NULL,
  `word_given` varchar(20) DEFAULT NULL,
  `Tries_given` int(20) DEFAULT NULL,
  `Tries_used` int(20) DEFAULT NULL,
  `Game_outcome` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `game_results`
--

INSERT INTO `game_results` (`Game_No`, `word_given`, `Tries_given`, `Tries_used`, `Game_outcome`) VALUES
(1, 'INFORMATION', 11, 2, 'WON'),
(2, 'HANGMAN', 7, 3, 'WON'),
(3, 'AMERICA', 7, 7, 'LOST'),
(1, 'PYTHON', 6, 4, 'WON'),
(2, 'FOOTBALL', 8, 3, 'WON'),
(3, 'TECHNOLOGY', 10, 9, 'WON'),
(4, 'GHOST', 5, 5, 'LOST'),
(5, 'CONSOLE', 7, 7, 'LOST'),
(6, 'CRICKET', 7, 7, 'LOST'),
(7, 'ELEPHANT', 8, 1, 'WON'),
(8, 'CONSOLE', 7, 7, 'LOST');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
