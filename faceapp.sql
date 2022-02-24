-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 12, 2021 at 01:03 AM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 7.3.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `faceapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `name` varchar(255) DEFAULT NULL,
  `dtString` varchar(255) DEFAULT NULL,
  `dyString` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`name`, `dtString`, `dyString`) VALUES
('jonathan', '23:46:48', '10-08-21'),
('akash', '23:46:48', '10-08-21'),
('eeshan', '23:46:48', '10-08-21'),
('eeshan', '23:47:26', '11-08-21'),
('akash', '23:48:32', '12-08-21'),
('jonathan', '23:57:40', '13-08-21'),
('akash', '23:57:40', '13-08-21'),
('jonathan', '23:59:43', '14-08-21'),
('eeshan', '05:25:54', '20-08-21'),
('hayson', '15:02:44', '22-08-21'),
('hayson', '15:15:22', '22-08-21'),
('nolan', '15:15:33', '22-08-21'),
('jonathan', '19:04:05', '28-08-21'),
('akash', '19:04:05', '28-08-21'),
('aditya', '21:31:50', '28-08-21'),
('jonathan', '21:34:57', '11-08-21'),
('akash', '21:34:57', '11-08-21');

-- --------------------------------------------------------

--
-- Table structure for table `studentinfo`
--

CREATE TABLE `studentinfo` (
  `rollno` int(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `totalattended` varchar(255) NOT NULL,
  `attendancepercent` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `studentinfo`
--

INSERT INTO `studentinfo` (`rollno`, `name`, `totalattended`, `attendancepercent`) VALUES
(4, 'Yohan', 'NULL', 'NULL'),
(5, 'eeshan', 'NULL', 'NULL'),
(6, 'aditya', 'NULL', 'NULL');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `studentinfo`
--
ALTER TABLE `studentinfo`
  ADD PRIMARY KEY (`rollno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `studentinfo`
--
ALTER TABLE `studentinfo`
  MODIFY `rollno` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
