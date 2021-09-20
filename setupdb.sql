CREATE DATABASE IF NOT EXISTS sensors
DROP TABLE IF EXISTS `data`;
CREATE TABLE data (
	data_id INT AUTO_INCREMENT PRIMARY KEY,
	time varchar(20),
	power INT,
	temp INT,
	humidity INT,
	light INT,
	co2 INT,
	dust DOUBLE
)

LOAD DATA INFILE '/docker-entrypoint-initdb.d/init_data/sensor-data.csv'
INTO TABLE sensors.data
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n' (time,power,temp,humidity,light,co2,dust);