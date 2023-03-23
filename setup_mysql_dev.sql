-- A new Database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- A new user hbnb_dev( in localhost). The password of hbnb_dev of hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- hbnb_dev should have all privileges on the database hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- hbnb_dev should have SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
