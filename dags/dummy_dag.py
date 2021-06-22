from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

with DAG('example_dag', start_date=datetime(2021, 5, 22)) as dag:
    op = DummyOperator(task_id='op')
