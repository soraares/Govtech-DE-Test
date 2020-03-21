FROM puckel/docker-airflow:latest

# copy over source code and other dependencies
# working direction ${AIRFLOW_USER_HOME} set to be /usr/local/airflow
COPY main.py dags/
COPY dataset.csv .
COPY setup.sh .

# add a volume to the container
# VOLUME /path/to/folder/containing/unprocessed/datasets

# create a new directory for saving processed files
RUN mkdir output/

# append working directory to path
ENV PATH=$PATH:${AIRFLOW_USER_HOME}

# give permissions to airflow user as root
USER root
RUN chown airflow .

# switch back to airflow user
USER airflow

# ports
EXPOSE 8080 5555 8793

# start webserver and scheduler
ENTRYPOINT [ "setup.sh" ]