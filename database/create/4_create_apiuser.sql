CREATE USER 'apiuser'@'%' IDENTIFIED BY 'apiuserpass';
GRANT ALL PRIVILEGES ON cs415website.* TO 'apiuser'@'%';
FLUSH PRIVILEGES;
