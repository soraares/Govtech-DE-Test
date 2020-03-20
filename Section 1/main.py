from airflow import DAG
from airflow.operators import PythonOperator
from datetime import datetime, timedelta
from utils import munge_data

# dag settings
default_args = {
    'owner': 'thomas',
    'depends_on_past': False,
    'start_date': datetime(2020, 3, 19),
    'email': ['soraares@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes = 1),
    'schedule_interval': '5 0 * * *'
}

dag = DAG(dag_id = 'data_munging', default_args = default_args)

task = PythonOperator(
    task_id = 'daily_data_munge',
    python_callable = munge_data,
    dag = dag,
)