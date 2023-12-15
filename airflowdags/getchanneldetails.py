import os
import pandas as pd
import googleapiclient.discovery
from sqlalchemy import create_engine
from googleapiclient.errors import HttpError
from dotenv import load_dotenv

def channel_details(**kwargs):
    pg_user = kwargs['pg_user']
    pg_password = kwargs['pg_password']
    pg_host = kwargs['pg_host']
    pg_db = kwargs['pg_db']
    pg_table = kwargs['pg_table']
    pg_port = kwargs['pg_port']

    # YouTube API key (replace with your actual key)
    api_key = "AIzaSyDa_tJy8h3_PD7BPUZqEE7sDWqYN5E0z6I"
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

    # PostgreSQL connection setup
    engine = create_engine(f"postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}")
    con = engine.connect()

    # Read channel IDs from the database
    tname = 'dbtschema.fact_trips'
    query = f"SELECT * FROM {tname}"
    channel_ids_df = pd.read_sql(query, engine)
    channel_ids_df.drop_duplicates(inplace = True)
    channel_ids_list = channel_ids_df['channelid'].tolist()

    # List to store channel data
    channel_data_list = []

    try:
        # Fetch details for each channel
        for channel_id in channel_ids_list:
            channel_response = youtube.channels().list(
                part='snippet,statistics',
                id=channel_id
            ).execute()

            if 'items' in channel_response and channel_response['items']:
                channel_details = channel_response['items'][0]

                # Append channel data to the list
                channel_data_list.append({
                    'channelid': channel_id,
                    'channeltitle': channel_details['snippet']['title'],
                    'channeldescription': channel_details['snippet']['description'],
                    'channelpublishedat': channel_details['snippet']['publishedAt'],
                    'channelcountry': channel_details['snippet'].get('country', ''),
                    'viewcounts': channel_details['statistics'].get('viewCount', 0),
                    'subscribercounts': channel_details['statistics'].get('subscriberCount', 0),
                    'videocounts': channel_details['statistics'].get('videoCount', 0),
                })

    except HttpError as e:
        print(f"An error occurred: {e}")

    print(f"Total channels processed: {len(channel_data_list)}")

    # Create a DataFrame from the channel data list
    channel_df = pd.DataFrame(channel_data_list)

    # Extract relevant columns and save to CSV
    data = channel_df[['channelid', 'channeltitle', 'channeldescription', 'channelpublishedat', 'channelcountry', 'viewcounts', 'subscribercounts', 'videocounts']]
    data.to_csv('dataset.csv', index=False)

if __name__ == "__main__":
    channel_details()
