# YOUTUBE DATA ENGINEERING PROJECT

## Navigating 2023's New Channel Success

## Introduction

Welcome to my YouTube Data Engineering Project. In this initiative, I will be providing valuable insights into YouTube channels created in the year 2023, delving into their development over the course of the year. This project serves as a platform for me to showcase my expertise in utilizing advanced big data tools. By leveraging these tools, I aim to derive meaningful insights, facilitate efficient data collection, and ensure a seamless transition in the realm of data analytics. Join me as we explore the intricate dynamics of YouTube channel evolution through the lens of data engineering.


## Overview
YouTube is an American online video-sharing and social media platform that is owned by Google. Accessible globally, it stands as the second most visited website, surpassed only by Google itself. Every minute witnesses an astonishing 694,000 hours of video being streamed on YouTube, establishing it as a significant medium. Over the years, YouTube has evolved into a lucrative source of income for many individuals. A "YouTuber" is an individual who engages in the creation and dissemination of content on the YouTube platform.

The financial remuneration for YouTubers is diverse, emanating from various channels. If we exclusively consider earnings from YouTube's Partner Program, YouTubers accrue an average of $18 per 1,000 views. However, this is contingent upon meeting eligibility criteria, including a minimum of 1,000 subscribers and 4,000 watch hours within the preceding 12 months.

This project will specifically concentrate on YouTubers who initiated their channels in the year 2023, delving into their progress and achievements. While YouTube serves as a platform where substantial financial gains can be realized by content creators, it is imperative to acknowledge the inherent challenges faced by newcomers in every entrepreneurial endeavor.

## Architecture & Technologies
This architectural framework ensures a streamlined, automated, and scalable approach to handling YouTube channel data, from its extraction to transformation and final visualization.


![youtubearchitecture (1)](https://github.com/BrightOsas/Youtube-data-pipeline/assets/98474404/02cec5cb-f0cd-46a8-9d7b-ec637a89ddb1)  

    

1. Docker: Containerization  
2. Apache Airflow: Orchestration
3. YouTube API Integration: New channels are extracted using the YouTube API.  
4. PostgreSQL Database: Extracted new channels are stored in a PostgreSQL database.  
5. Data Extraction: ChannelID data is extracted from the database.  
6. YouTube Data Update: Extracted data is sent back to YouTube using the YouTube API to retrieve updated statistics and snippet information.  
7. Boto3: Batch processing of the collected data.  
8. AWS S3 Storage: Collected data is transferred to an AWS S3 bucket.  
9. AWS Lambda Function: A Lambda function is triggered upon the arrival of data in the S3 bucket.  
10. AWS CloudWatch: Logging Lambda function execution and monitoring Lambda metrics.  
11. AWS Redshift Serverless Database: Lambda initiates the data upload to an AWS Redshift Serverless Data Warehouse.  
12. DBt Cloud: Scheduled weekly, DBt Cloud runs transformation processes on the data.  
13. Looker Studio: The finalized data is visualized on Data Studio.


## How to run the pipeline
* cd ./airflow
* docker-compose up -d
* cd ./postgres
* docker-compose up -d

-- Airflow Dags TreeView 
![airflow1](https://github.com/BrightOsas/Youtube-data-pipeline/assets/98474404/20afb423-411f-44bd-8747-62e826954f4c)  

-- AWS Lambda Task  
Cloudwatch logs  
![statcdwatch](https://github.com/BrightOsas/Youtube-data-pipeline/assets/98474404/88d21c9b-e28b-4340-976b-a0a1c6006fd4)
![snippetcloudwatch](https://github.com/BrightOsas/Youtube-data-pipeline/assets/98474404/0897952a-802e-44cc-b442-50c4396c7a18)  

-- DBT Jobs  
Lineage graph
![dbt4](https://github.com/BrightOsas/Youtube-data-pipeline/assets/98474404/629c5641-130e-4e51-ab07-9d04984ffa61)  

DBT Scheduler
![dbt2](https://github.com/BrightOsas/Youtube-data-pipeline/assets/98474404/13e59071-9ca7-420f-930e-235dc9e01f3d)  

DBT Documentation
![dbt5](https://github.com/BrightOsas/Youtube-data-pipeline/assets/98474404/18876cea-0249-4410-bfeb-233a8a4bd79d)

 
## Result
![ytdb](https://github.com/BrightOsas/Youtube-data-pipeline/assets/98474404/d5d7b78d-b599-445e-9757-0cf098087bdb)

To be eligible for YouTube's Partner Program, a YouTube channel must have a minimum of 1000 subscribers and 4,000 watch hours within the preceding 12 months. Excluding the 12-month criteria, let's analyze the percentage of channels from each month with over 1,000 subscribers and 4,000 watch hours.  
![newcrit](https://github.com/BrightOsas/Youtube-data-pipeline/assets/98474404/bb2473fa-7278-4e33-b126-cec4fbdc8dcf)

## Requirement
* To search for a channel using the channel ID 'youtube.com/channel/channel_id'   
* [Follow this link to read about the YouTube API](https://developers.google.com/youtube/v3/docs/)  
* [Follow this link to obtain a YouTube API key](https://console.cloud.google.com/apis)  
* Docker desktop
* AWS account


## contact
* [Bright Osarenren](linkedin.com/in/brightosas)
* [Project link](https://github.com/BrightOsas/Youtube-Data-Pipeline)
