import os
import pandas as pd
from datetime import datetime, timedelta
import googleapiclient.discovery
from googleapiclient.errors import HttpError


def getnewchannelid():

    api_key = os.getenv("API_KEY1")
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

    current_date = datetime.now()
    start_date = (current_date - timedelta(days=1)).strftime('%Y-%m-%dT00:00:00Z')
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
    newchannel_df = pd.DataFrame(channel_ids)
    newchannel_df.to_csv('newchannels.csv', index = False)

if __name__ == "__main__":
    getnewchannelid()

def getsnippet():
    channel_ids_list = pd.read_csv("channel_ids.csv")
    channel_ids_list = channel_ids_list['channelid'].tolist()

    api_key = os.getenv("API_KEY2")
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

    channel_data_list = []

    try:

        for channel_id in channel_ids_list:
            channel_response = youtube.channels().list(
                part='snippet',
                id=channel_id
            ).execute()

            if 'items' in channel_response and channel_response['items']:
                channel_details = channel_response['items'][0]

                channel_data_list.append({
                    'channelid': channel_id,
                    'channeltitle': channel_details['snippet']['title'],
                    'channeldescription': channel_details['snippet']['description'],
                    'channelpublishedat': channel_details['snippet']['publishedAt'],
                    'channelcountry': channel_details['snippet'].get('country', ''),
                })

    except HttpError as e:
        print(f"An error occurred: {e}")

    print(f"Total channels processed: {len(channel_data_list)}")

    channel_df = pd.DataFrame(channel_data_list)

    snippetdata = channel_df[['channelid', 'channeltitle', 'channeldescription', 'channelpublishedat', 'channelcountry']]
    snippetdata.to_csv("snippetdata.csv", index= False )

    if __name__ == "__main__":
        getsnippet()


def getstat():
    
    channel_ids_list = pd.read_csv("channel_ids.csv")
    channel_ids_list = channel_ids_list['channelid'].tolist()

    api_key = os.getenv("API_KEY3")
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

    channel_data_list = []

    try:
        for channel_id in channel_ids_list:
            channel_response = youtube.channels().list(
                part='statistics',
                id=channel_id
            ).execute()

            if 'items' in channel_response and channel_response['items']:
                channel_details = channel_response['items'][0]

                channel_data_list.append({
                    'channelid': channel_id,
                    'viewcounts': channel_details['statistics'].get('viewCount', 0),
                    'subscribercounts': channel_details['statistics'].get('subscriberCount', 0),
                    'videocounts': channel_details['statistics'].get('videoCount', 0),
                })

    except HttpError as e:
        print(f"An error occurred: {e}")

    print(f"Total channels processed: {len(channel_data_list)}")

    channel_df = pd.DataFrame(channel_data_list)

    statdata = channel_df[['channelid', 'viewcounts','subscribercounts','videocounts']]
    statdata.to_csv("statdata.csv", index= False )

if __name__ == "__main__":
    getstat()
