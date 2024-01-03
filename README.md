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

* YouTube API Integration: New channels are extracted using the YouTube API
* PostgreSQL Database: Extracted data is stored in a PostgreSQL database
* YouTube Data Update: Channel ID data is extracted and sent back to YouTube to retrieve updated statistics and snippet information
* AWS S3 Storage: Collected data is seamlessly transmitted to an AWS S3 bucket
* AWS Lambda Function: A Lambda function is triggered upon data arrival in the S3 bucket, initiating the upload of data to an AWS Redshift Serverless Data Warehouse
* DBt Cloud: Scheduled weekly, DBt Cloud runs transformation processes on the data
* AWS Redshift Serverless Database: Transformed data is reloaded back into the Redshift Serverless Database
* Looker Studio: The finalized data is then visualized on Data Studio
* Docker: Containerization  
* Apache Airflow: Orchestration   
* Terraform: Infrastructure as Code (IaaC)  
* Boto3: Batch Processing  
* Python: Scripting


  
## Result

## contact
* [Bright Osarenren](linkedin.com/in/brightosas)
* [Project link](https://github.com/BrightOsas/Youtube-Data-Pipeline)
