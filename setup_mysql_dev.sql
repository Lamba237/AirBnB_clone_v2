-- This script prepares a MySQL server for the project by creating a database and a user with specific privileges.

mysql -u root -p <<EOF
-- Create the database hbnb_dev_db if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user hbnb_dev if it doesn't already exist and set its password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the hbnb_dev_db database to the hbnb_dev user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the performance_schema database to the hbnb_dev user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush the privileges to ensure the changes take effect immediately
FLUSH PRIVILEGES;
EOF
