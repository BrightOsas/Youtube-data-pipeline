from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from databasedcon import dbconnectiontest, appendnewchannelid, getallchannelid
from fetchdata import getnewchannelid, getsnippet, getstat
from uploadtos3 import uploadsnippet2s3, uploadstat2s3

default_args = {
    "owner": 'bright',
    "retries": 2,
}


with DAG(
    dag_id = 'youtubepipeline',
    default_args=default_args,
    description = 'youtube data pipeline',
    start_date=datetime(2023, 12, 24),
    schedule_interval='@daily',
    catchup=False,

)as dag:
    connection2db = PythonOperator(
        task_id="TestDBconnection",
        python_callable=dbconnectiontest,
    )

fetchchannel = PythonOperator(
    task_id = 'FetchnewChannels',
    python_callable = getnewchannelid
)

uploadchannel = PythonOperator(
    task_id='UploadnewChannels',
    python_callable = appendnewchannelid
)

getchannel= PythonOperator(
      task_id = "GetallChannels",
      python_callable = getallchannelid,
   )

getsnippetdetails= PythonOperator(
       task_id = "Getsnippet",
       python_callable = getsnippet,
   )
    
getstatdetails= PythonOperator(
      task_id = "Getstats",
      python_callable = getstat
  )
uploadsnip2_s3 = PythonOperator(
    task_id = "UploadSnip2S3",
    python_callable = uploadsnippet2s3,
)

uploadstat2_s3 = PythonOperator(
    task_id = "UploadStat2S3",
    python_callable = uploadstat2s3,
)




connection2db  >> fetchchannel >> uploadchannel >> getchannel >> getsnippetdetails >> uploadsnip2_s3

connection2db  >> fetchchannel >> uploadchannel >> getchannel >> getstatdetails >> uploadstat2_s3
