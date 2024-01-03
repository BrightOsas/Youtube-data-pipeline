import os
import json
import psycopg2
import time
from datetime import datetime

def lambda_handler(event, context):
    print(f'event collected is {event}')
    for record in event['Records']:
        s3_bucket = record['s3']['bucket']['name']
        print(f's3_bucket name is {s3_bucket}')
        s3_key = record['s3']['object']['key']
        filepath = f"s3://{s3_bucket}/{s3_key}"
        print(f'filepath: {filepath}')
        aws_key = os.getenv('aws_key')
        aws_secret = os.getenv('aws_secret')
        dbname = os.getenv('dbname')
        host = os.getenv('host')
        user = os.getenv('user')
        password = os.getenv('password')

        if 'snippet.csv' in s3_key:
            tablename = "channelsnippet"
        elif 'statistic.csv' in s3_key:
            tablename = "channelstat"

        try:
            with psycopg2.connect(dbname=dbname, host=host, port=5439, user=user, password=password) as con:
                print('connection successful')
                with con.cursor() as cur:

                    # Truncate the table before loading new data
                    truncate_query = f"TRUNCATE TABLE {tablename};"
                    cur.execute(truncate_query)
                    con.commit()
                    print(f'{tablename} table is truncated')

                    query = "COPY {} FROM '{}' CREDENTIALS 'aws_access_key_id={};aws_secret_access_key={}' CSV IGNOREHEADER 1;".format(tablename, filepath, aws_key, aws_secret)
                    print("query is {}".format(query))
                    
                    cur.execute(query)
                    print('query is executed....')
                    con.commit()
                    print('connection closed....')
                    print('ETL process completed')
        except Exception as e:
            print(f"Error processing file {s3_key}: {e}")
