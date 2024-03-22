CREATE USER 'apiuser'@'localhost' IDENTIFIED BY 'apiuserpass';
CREATE USER 'apiuser'@'%' IDENTIFIED BY 'apiuserpass';
GRANT ALL PRIVILEGES ON *.* TO 'apiuser'@'localhost' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO 'apiuser'@'%', 'apiuser'@'172.29.0.2' WITH GRANT OPTION;
FLUSH PRIVILEGES;
