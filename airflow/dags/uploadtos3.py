import pandas as pd
import boto3
import os

def uploadsnippet2s3():
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

    s3 = boto3.client('s3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )

    bucket_name = "brightyoutubes3"
    s3_key = 'snippet.csv'
    local_file_path = "snippetdata.csv"

    try:
        s3.upload_file(local_file_path, bucket_name, s3_key)
        print(f"File uploaded successfully to S3: {s3_key}")

    except Exception as e:
        print(f"An error occurred during S3 upload: {e}")

if __name__ == "__main__":
    uploadsnippet2s3()


def uploadstat2s3():
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

    s3 = boto3.client('s3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )

    bucket_name = "brightyoutubes3"
    s3_key = 'statistic.csv'
    local_file_path = "statdata.csv"

    try:
        s3.upload_file(local_file_path, bucket_name, s3_key)
        print(f"File uploaded successfully to S3: {s3_key}")

    except Exception as e:
        print(f"An error occurred during S3 upload: {e}")

if __name__ == "__main__":
    uploadstat2s3()

