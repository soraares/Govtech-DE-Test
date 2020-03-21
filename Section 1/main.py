import pandas as pd
import os
from datetime import datetime, timedelta

env_vars = os.environ
file_path = env_vars['HOME']

def munge_data(file = file_path + '/dataset.csv'):
    df = pd.read_csv(file)

    # remove missing names then split into first and last names
    df = df[(pd.notna(df['name'])) | ~ (df['name'] == '')]
    df['last_name'] = df['name']
    df.rename(columns = {'name': 'first_name'}, inplace = True)
    df['first_name'] = df['first_name'].apply(lambda x: x.split(' ')[0])
    df['last_name'] = df['last_name'].apply(lambda x: x.split(' ')[1])
    df = df[['first_name', 'last_name', 'price']]

    # remove leading 0's and check if price > 100
    df['price'] = df['price'].apply(str)
    df['price'] = df['price'].apply(lambda x: x.lstrip('0'))
    df['price'] = df['price'].apply(float)
    df['above_100'] = df['price'].apply(lambda x: x > 100)

    # save the output
    df.to_csv(f'{file_path}/output/dataset_{datetime.today().strftime("%Y%m%d")}.csv', index = False)
    
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils import timezone
import pendulum

# set local timezone
local_tz = pendulum.timezone("Singapore")

# dag settings
default_args = {
    'owner': 'thomas',
    'depends_on_past': False,
    'email': ['soraares@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes = 30)
}

## set the schedule to run the data processing job
dag = DAG(dag_id = 'data_munging',
        start_date =  datetime(2020, 3, 21),
        schedule_interval = '5 1 * * *',
        catchup = False,
        default_args = default_args
        )

task = PythonOperator(
    task_id = 'daily_data_munge',
    python_callable = munge_data,
    dag = dag
)