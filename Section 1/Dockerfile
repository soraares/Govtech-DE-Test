FROM puckel/docker-airflow:latest

# copy over source code and other dependencies
COPY . ./dags

# give permissions to airflow user
USER root
RUN chown airflow ./dags

# switch back to airflow user
USER airflow