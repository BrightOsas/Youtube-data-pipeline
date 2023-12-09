import os
import pandas as pd
import googleapiclient.discovery
from datetime import datetime
from googleapiclient.errors import HttpError
import argparse
from dotenv import load_dotenv


def main():
    api_key = input("API key: ")
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

    def get_date_input(prompt):
        while True:
            try:
                date_str = input(prompt)
                date_obj = datetime.strptime(date_str, "%Y-%m-%d")
                return date_obj
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

    start_date = get_date_input("Enter the start date (YYYY-MM-DD): ").strftime('%Y-%m-%dT00:00:00Z')
    end_date = get_date_input("Enter the end date (YYYY-MM-DD): ").strftime('%Y-%m-%dT23:59:59Z')

    channel_data_list = []

    try:
        next_page_token = None

        while True:
            # Execute the YouTube API search with the date range filter and pagination
            channels = youtube.search().list(
                part='id,snippet',
                type='channel',
                q='',
                order='relevance',
                maxResults=100,
                publishedAfter=start_date,
                publishedBefore=end_date,
                pageToken=next_page_token
            ).execute()

            # Extract channel information from the current page and add them to the list
            for item in channels.get('items', []):
                channel_id = item['id']['channelId']

                # Execute another request to retrieve channel details
                channel_response = youtube.channels().list(
                    part='snippet,statistics,topicDetails',
                    id=channel_id
                ).execute()

                channel_details = channel_response.get('items', [])[0]

                # Append data to the list
                channel_data_list.append({
                    'channelid': channel_id,
                    'channeltitle': channel_details['snippet']['title'],
                    'channeldescription': channel_details['snippet']['description'],
                    'channelpublishedat': channel_details['snippet']['publishedAt'],
                    'defaultlanguage': channel_details['snippet'].get('defaultLanguage', ''),
                    'channelcountry': channel_details['snippet'].get('country', ''),
                    'viewcounts': channel_details['statistics'].get('viewCount', 0),
                    'subscribercounts': channel_details['statistics'].get('subscriberCount', 0),
                    'videocounts': channel_details['statistics'].get('videoCount', 0),
                    'hiddensubscribescount': channel_details['statistics'].get('hiddenSubscriberCount', 0),
                    'topicCategories':channel_details['topicDetails'].get('topicCategories',0)
                })

            # Check if there are more pages of results
            next_page_token = channels.get('nextPageToken')

            # Exit the loop if there are no more pages
            if not next_page_token:
                break

    except HttpError as e:
        print(f"An error occurred: {e}")

    print(f"Total channels processed: {len(channel_data_list)}")

    # Create DataFrames
    channel_df = pd.DataFrame(channel_data_list)

    # Separate DataFrames
    snippet_df = channel_df[['channelid', 'channeltitle', 'channeldescription', 'channelpublishedat', 'defaultlanguage', 'channelcountry','topicCategories']]
    statistics_df = channel_df[['channelid', 'viewcounts', 'subscribercounts', 'videocounts', 'hiddensubscribescount']]

    snippet_df.to_csv('snippet_datafebnew2.csv', index=False)
    statistics_df.to_csv('statistics_datafebnew2.csv', index=False)

if __name__ == "__main__":
    main()



