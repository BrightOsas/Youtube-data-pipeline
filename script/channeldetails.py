import os
import pandas as pd
import googleapiclient.discovery
from datetime import datetime
from googleapiclient.errors import HttpError
from dotenv import load_dotenv


def main():
    api_key = "AIzaSyDa_tJy8h3_PD7BPUZqEE7sDWqYN5E0z6I"
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

    channel_ids_df = pd.read_csv("channel_ids2.csv")
    channel_ids_list = channel_ids_df['channelid'].tolist()

    channel_data_list = []

    try:
        for channel_id in channel_ids_list:
            # Execute a request to retrieve channel details
            channel_response = youtube.channels().list(
                part='snippet,statistics',
                id=channel_id
            ).execute()

            # Check if 'items' is not empty
            if 'items' in channel_response and channel_response['items']:
                channel_details = channel_response['items'][0]

                # Append data to the list
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

    # Create DataFrames
    channel_df = pd.DataFrame(channel_data_list)

    # Separate DataFrames
    dataset = channel_df[['channelid', 'channeltitle', 'channeldescription', 'channelpublishedat', 'channelcountry', 'viewcounts', 'subscribercounts', 'videocounts']]

    dataset.to_csv('dataset.csv', index=False)

if __name__ == "__main__":
    main()