import os
import pandas as pd
import googleapiclient.discovery
from sqlalchemy import create_engine
from datetime import datetime, timedelta
from googleapiclient.errors import HttpError
from dotenv import load_dotenv

def main(**kwargs):
    load_dotenv() 
    pg_user = kwargs['pg_user']
    pg_password = kwargs['pg_password']
    pg_host = kwargs['pg_host']
    pg_db = kwargs['pg_db']
    pg_table = kwargs['pg_table']
    ytripfile = kwargs['ytripfile']
    pg_port = kwargs['pg_port']

    engine = create_engine(f"postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}")
    con = engine.connect()

    api_key = "AIzaSyDa_tJy8h3_PD7BPUZqEE7sDWqYN5E0z6I" # Use environment variables for sensitive data

    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)


    # Calculate the start date (current date - 7 days) and end date (current date - 1 day)
    current_date = datetime.now()
    start_date = (current_date - timedelta(days=7)).strftime('%Y-%m-%dT00:00:00Z')
    end_date = (current_date - timedelta(days=1)).strftime('%Y-%m-%dT23:59:59Z')

    channel_ids = []  # Store only channelids

    try:
        next_page_token = None

        while True:
            # Execute the YouTube API search with the date range filter and pagination
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

            # Extract channel IDs from the current page and add them to the list
            for item in channels.get('items', []):
                channel_id = item['id']['channelId']
                channel_ids.append({'channelid': channel_id})

            # Check if there are more pages of results
            next_page_token = channels.get('nextPageToken')

            # Exit the loop if there are no more pages
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
    main()
