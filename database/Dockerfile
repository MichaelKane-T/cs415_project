FROM mysql

# Set environment variables
ENV MYSQL_ROOT_PASSWORD=apiuserpass

# Copy SQL script to create user and grant privileges
COPY ./create /docker-entrypoint-initdb.d
EXPOSE 3306