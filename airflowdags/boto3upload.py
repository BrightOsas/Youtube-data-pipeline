import pandas as pd
import boto3
import os
def upload_to_s3():
    s3 = boto3.client('s3')
    bucket_name = "brighttaxitrips3bucket"
    s3_key = os.getenv("S3 KEY")

    data = pd.read_csv("dataset.csv") 

    with open("/tmp/dataset.csv", "w") as tmp_file:
        data.to_csv(tmp_file, index=False)

    s3.upload_file("/tmp/dataset.csv", bucket_name, s3_key)