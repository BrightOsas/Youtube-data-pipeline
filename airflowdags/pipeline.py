import os
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

from newchannel import new_channelid
from getchanneldetails import channel_details
from dbconnect import dbconnectiontest
from boto3upload import upload_to_s3

default_args = {
    "owner": 'bright',
    "retries": 1,
}

PG_HOST = os.getenv('PG_HOST')
PG_USER = os.getenv('PG_USER')
PG_PASSWORD = os.getenv('PG_PASSWORD')
PG_PORT = int(os.getenv('PG_PORT'))
PG_DATABASE = os.getenv('PG_DATABASE')
PG_TABLE = os.getenv('PG_TABLE')

with DAG(
    dag_id = 'youtubepipeline',
    default_args=default_args,
    description = 'youtube new channels data pipeline',
    start_date=datetime(2023, 12, 1),
    schedule_interval='@daily',

)as dag:
    connection2db = PythonOperator(
        task_id="test_db_connection",
        python_callable=dbconnectiontest,
    )
    getnewchannel= PythonOperator(
        task_id = "importingyellowdata",
        python_callable = new_channelid,
        op_kwargs=dict(
            pg_user=PG_USER,
            pg_password=PG_PASSWORD,
            pg_host=PG_HOST,
            pg_db=PG_DATABASE,
            pg_table=PG_TABLE,
            pg_port=PG_PORT

        )
    )

    getchanneldetails= PythonOperator(
        task_id = "importinggreendata",
        python_callable = channel_details,
        op_kwargs=dict(
            pg_user=PG_USER,
            pg_password=PG_PASSWORD,
            pg_host=PG_HOST,
            pg_db=PG_DATABASE,
            pg_table=PG_TABLE,
            pg_port=PG_PORT
        )
    )

    upload_task = PythonOperator(
        task_id='upload_to_s3_task',
        python_callable=upload_to_s3,
    )
connection2db >> getnewchannel >> getchanneldetails >> upload_task