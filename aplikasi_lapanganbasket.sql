-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 27 Bulan Mei 2021 pada 11.10
-- Versi server: 10.4.18-MariaDB
-- Versi PHP: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aplikasi_lapanganbasket`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `tbbooking`
--

CREATE TABLE `tbbooking` (
  `no_id` varchar(12) NOT NULL,
  `tanggal` varchar(20) NOT NULL,
  `pilihan` varchar(50) NOT NULL,
  `nama_club` varchar(250) NOT NULL,
  `asal_club` varchar(250) NOT NULL,
  `captain` varchar(250) NOT NULL,
  `no_hp` varchar(50) NOT NULL,
  `banyak_pemain` varchar(20) NOT NULL,
  `waktu_mulai` varchar(100) NOT NULL,
  `waktu_akhir` varchar(50) NOT NULL,
  `keterangan` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `tbbooking`
--

INSERT INTO `tbbooking` (`no_id`, `tanggal`, `pilihan`, `nama_club`, `asal_club`, `captain`, `no_hp`, `banyak_pemain`, `waktu_mulai`, `waktu_akhir`, `keterangan`) VALUES
('323798313052', '27/05/2021', 'Lapangan 2 - Kaguya ', 'gj war army', 'pasuruan', 'fulan', '55665', '5', '00:00', '05:00', '-'),
('836263373197', '05/01/2020', 'Lapangan 1 - Surya', 'army', 'pasuruan', 'fulana', '881036102146', '30', '00:01', '00:05', 'Lunas conk');

-- --------------------------------------------------------

--
-- Struktur dari tabel `tblogin`
--

CREATE TABLE `tblogin` (
  `username` varchar(20) NOT NULL,
  `nama_lengkap` varchar(100) NOT NULL,
  `tanggal_lahir` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `tblogin`
--

INSERT INTO `tblogin` (`username`, `nama_lengkap`, `tanggal_lahir`, `password`, `email`) VALUES
('admin', 'admin', '01/01/2000', 'a', 'admin@gamil.com'),
('Amani', 'AmaniTech', '24/11/2001', 'amani', 'amanitech@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `tbbooking`
--
ALTER TABLE `tbbooking`
  ADD PRIMARY KEY (`no_id`);

--
-- Indeks untuk tabel `tblogin`
--
ALTER TABLE `tblogin`
  ADD PRIMARY KEY (`username`,`password`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
