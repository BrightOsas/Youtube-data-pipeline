import os
import pandas as pd
from sqlalchemy import create_engine
from airflow.providers.postgres.hooks.postgres import PostgresHook

host = os.getenv("HOST")
port = int(os.getenv("PORT"))
user = os.getenv("USER")
password = os.getenv("PASSWORD")
db = os.getenv("DB")
pg_table = os.getenv("TABLE")

def dbconnectiontest():
    #Confirm database is running and accepting connections
    try:
        hook = PostgresHook(postgres_conn_id='postgrescon')
        conn = hook.get_conn()

        print("PostgreSQL connection successful")
    except Exception as e:
        print("PostgreSQL connection failed:", str(e))
        raise



def appendnewchannelid():
    # Read data from the CSV file into a DataFrame
    channel_df = pd.read_csv('channel_df.csv')

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    # Append new channels fetched to the existing channels table
    channel_df.to_sql(con=engine, name=pg_table, if_exists='append', index=False)
    
if __name__ == "__main__":
    appendnewchannelid()


def getallchannelid():

    hook = PostgresHook(postgres_conn_id='postgrescon')
    con = hook.get_conn()

    # Fetch channelids from the database
    query = f"SELECT * FROM {pg_table}"
    channel_ids_df = pd.read_sql(query, con)
    channel_ids_df.drop_duplicates(inplace = True)
    channel_ids_df.to_csv("channel_ids.csv", index=False)

    con.close()

if __name__ == "__main__":
    getallchannelid()










