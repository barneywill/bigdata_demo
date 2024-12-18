import os
import logging
import time
from datetime import timedelta, datetime

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.template import literal

from script.test_py import say_bye

def say_hello(name, date):
    time.sleep(10)
    print(f"hello {name} on {date}")

default_args = {
    'owner' : 'admin',
    'start_date' : datetime(2024, 12, 18) #days_ago(1)
}

with DAG(
    dag_id = 'test_dag',
    default_args=default_args,
    schedule_interval='0 * * * *', #'@once'
    catchup=False
) as dag:
    
    start_task = DummyOperator(task_id='start_task')
    
    bash_task = BashOperator(
        task_id='bash_task',
        bash_command='pwd & sleep 5 & echo "running at: {{ds}}, {{execution_date.strftime("%Y-%m-%d %H:%M:%S")}}"'
    )
    
    script_bash_task = BashOperator(
        task_id='script_bash_task',
        bash_command=literal('/path/to/script/test_sh.sh'),
        env={'CURRENT_DATE':'{{ds}}'}
    )

    python_task = PythonOperator(
        task_id='python_task',
        python_callable=say_hello,
        op_kwargs={'name':'admin','date':'{{ds}}'}
    )

    script_python_task = PythonOperator(
        task_id='script_python_task',
        python_callable=say_bye,
        op_kwargs={'name':'admin','date':'{{ds}}'}
    )

    start_task >> [bash_task, script_bash_task] >> python_task >> script_python_task