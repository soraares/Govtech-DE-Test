FROM postgres:latest

# all files added to /docker-entrypoint-initdb.d will be run upon a cold start of the container
COPY setup.sql /docker-entrypoint-initdb.d

EXPOSE 5432