CREATE USER 'apiuser'@'localhost' IDENTIFIED BY 'apiuserpass';
CREATE USER 'apiuser'@'%' IDENTIFIED BY 'apiuserpass';
GRANT ALL PRIVILEGES ON *.* TO 'apiuser'@'localhost' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO 'apiuser'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
