## Airflow Setup Instructions

1. Install docker from [here](https://docs.docker.com/install/). Start docker.
2. Build the docker image from the dockerfile by entering `docker build -t airflow:1.0 .`.
3. Run the image by entering `docker run -d --name airflow -p 8080:8080 -e LOAD_EX=n airflow:1.0`.
4. Access the airflow UI at http://192.168.99.100:8080/admin/ (docker-machine ip default) or http://localhost:8080/admin, depending on your docker installation type. This may take some time as the container is setting up airflow. To check for any errors in the setting up process, run `docker logs airflow` to view the container logs.
5. Find the *dag* `data_munging`, and toggle the slider to the left of it to be on (the default is off).
6. The `data_munging` task will now run according to the schedule indicated. The cleaned datasets can be accessed by entering `docker cp airflow:/usr/local/airflow/output ./`, which will copy the folder containing all cleaned dataset to the current directory. The datasets are named in accordance of the time that they were processed. A sample of the dataset before and after cleaning is provided. (dataset.csv and cleaned_dataset.csv respectively)
7. A volume containing the files to be processed can be attached to the container to allow the container to perform the data munging directly on the files in the host system without needing to copy files. The volume should reference the filepath in the host system where data files will be made available periodically. An example of how to add a volume can be found in the dockerfile. 
8. (Cleanup) To stop the container, enter `docker stop airflow`. To remove the container, enter `docker rm -f airflow`.