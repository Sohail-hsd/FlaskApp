-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 20, 2021 at 09:19 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hsd`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `phone_num` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `msg` text NOT NULL,
  `date` date DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`sno`, `name`, `phone_num`, `email`, `msg`, `date`) VALUES
(1, 'First Post', '1234567890', 'first@gmail.com', 'First Massage...!', '2021-03-23'),
(3, 'Sohail HSD', '304444444444', 'Test@gmail.com', 'This is a test massage..!\r\n', '2021-03-23'),
(5, 'sohail HSD', '03440503646', 'Ali Mulla', 'Rasha kana', '2021-03-23'),
(6, 'sohail HSD', '03440503646', 'knight.hsd19@gmail.c', 'Test Msg', '2021-04-29');

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

CREATE TABLE `post` (
  `Sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `subheading` varchar(25) DEFAULT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp(),
  `img_file` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `post`
--

INSERT INTO `post` (`Sno`, `title`, `subheading`, `slug`, `content`, `date`, `img_file`) VALUES
(1, 'The First post by Sohail HSD. Content Upgraded..!', 'HSD is learning Flask', 'first-post', 'This is my first blog in flask, its fun, i am getting excited to to learn more about flask.\r\n\r\nContent Upgraded.!\r\n        ', '2021-03-28', 'picp.jpg'),
(3, 'This is 3rd Post, posted by SoHaIl HSD...!', '3rd Post.!', '3rd-post', 'The content of #3rd Post...!', '0000-00-00', 'picb.jpg'),
(6, 'DataBase system assignment # 1 By Sohail Muhammad', 'edit', 'post-edit', 'content', '2021-03-27', 'picb.jpg'),
(7, 'DataBase system assignment # 1 By Sohail Muhammad', 'The Subheadding is here', 'post-edit', 'content', '2021-03-27', 'picb.jpg'),
(8, 'DataBase system assignment # 1 By Sohail Muhammad', 'The Subheadding is here', 'post-edit', 'content', '2021-03-27', 'picb.jpg'),
(9, 'DataBase system assignment # 1 By Sohail Muhammad', 'The Subheadding is here', 'post-edit', 'content', '2021-03-27', 'picb.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`Sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `post`
--
ALTER TABLE `post`
  MODIFY `Sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
