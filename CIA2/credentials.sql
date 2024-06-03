create database mlt;
use mlt;

create table users(
	Name char(50),
    Email varchar(100),
    Password varchar(50)
);

insert into users values
('shreya','shreya@gmail.com','shreya');

select * from users;
