import os
import pandas as pd
import googleapiclient.discovery
from sqlalchemy import create_engine
from datetime import datetime, timedelta
from googleapiclient.errors import HttpError
from dotenv import load_dotenv

def new_channelid():
    load_dotenv() 
    pg_user = os.getenv('PG_USER')
    pg_password = os.getenv('PG_PASSWORD')
    pg_host = os.getenv('PG_HOST')
    pg_db = os.getenv('PG_DB')
    pg_table = os.getenv('PG_TABLE')
    pg_port = os.getenv('PG_PORT')
    api_key = os.getenv('API_KEY')

    engine = create_engine(f"postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}")
    con = engine.connect()

    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

    current_date = datetime.now()
    start_date = (current_date - timedelta(days=7)).strftime('%Y-%m-%dT00:00:00Z')
    end_date = (current_date - timedelta(days=1)).strftime('%Y-%m-%dT23:59:59Z')

    channel_ids = []  

    try:
        next_page_token = None

        while True:
            channels = youtube.search().list(
                part='id',
                type='channel',
                q='',
                order='relevance',
                maxResults=100,
                publishedAfter=start_date,
                publishedBefore=end_date,
                pageToken=next_page_token
            ).execute()

            for item in channels.get('items', []):
                channel_id = item['id']['channelId']
                channel_ids.append({'channelid': channel_id})

            next_page_token = channels.get('nextPageToken')

            if not next_page_token:
                break

    except HttpError as e:
        print(f"An error occurred: {e}")

    print(f"Total channels processed: {len(channel_ids)}")

    # Create DataFrame
    channel_df = pd.DataFrame(channel_ids)

    # Save channelids to a postgresdatabase
    channel_df.to_sql(con=con, name=pg_table, if_exists='append', index=False)

if __name__ == "__main__":
    new_channelid()
