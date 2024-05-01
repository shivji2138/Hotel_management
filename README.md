# SQL Qurey
CREATE DATABASE hotel_management;
USE hotel_management;

CREATE TABLE rooms (
    room_number INT PRIMARY KEY,
    capacity INT,
    price DECIMAL(10, 2),
    available BOOLEAN
);

CREATE TABLE reservations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    room_number INT,
    guest_name VARCHAR(255),
    check_in_date DATE,
    check_out_date DATE,
    FOREIGN KEY (room_number) REFERENCES rooms(room_number)
);
