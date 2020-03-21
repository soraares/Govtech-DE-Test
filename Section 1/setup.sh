#!/bin/bash

FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")
export FERNET_KEY=$FERNET_KEY

airflow initdb
sleep 2
(airflow webserver -p 8080 & )
sleep 2
airflow scheduler