FROM mysql

# Set environment variables
ENV MYSQL_DATABASE=cs415website \
    MYSQL_USER=apiuser \
    MYSQL_PASSWORD=apiuserpass \
    MYSQL_ROOT_PASSWORD=root_password

# Copy SQL script to create user and grant privileges
COPY ./create /docker-entrypoint-initdb.d
EXPOSE 3306