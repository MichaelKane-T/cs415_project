FROM mysql

ENV MYSQL_ROOT_PASSWORD=apiuserpass
COPY ./create /docker-entrypoint-initdb.d
EXPOSE 3306