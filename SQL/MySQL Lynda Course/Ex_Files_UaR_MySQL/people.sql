CREATE TABLE people (
first_name varchar(50) NOT NULL DEFAULT '',
last_name varchar(50) NOT NULL DEFAULT '',
mobile varchar(20) NOT NULL DEFAULT '',
birthday date DEFAULT NULL,
PRIMARY KEY (first_name,last_name,birthday)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
