import pandas as pd
from airflow.providers.postgres.hooks.postgres import PostgresHook

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

    pg_schema = 'public'
    pg_table = 'channels'

    channel_df = pd.read_csv("newchannels.csv")
    hook = PostgresHook(postgres_conn_id='postgrescon')
    con = hook.get_conn()

    #Append new channels fetched to exisiting channels table
    query = f"INSERT INTO {pg_schema}.{pg_table} SELECT * FROM channels"

    cursor = con.cursor()
    cursor.execute(query)
    con.commit()
    
if __name__ == "__main__":
    appendnewchannelid()


def getallchannelid():

    hook = PostgresHook(postgres_conn_id='postgrescon')
    con = hook.get_conn()

    # Fetch channelids from the database
    pg_table = 'channels'
    query = f"SELECT * FROM {pg_table} limit 10"
    channel_ids_df = pd.read_sql(query, con)
    channel_ids_df.drop_duplicates(inplace = True)
    channel_ids_df.to_csv("channel_ids.csv", index=False)

    con.close()

if __name__ == "__main__":
    getallchannelid()





