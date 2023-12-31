FROM python:3.9

WORKDIR /app
RUN pip install pandas sqlalchemy psycopg2 arg
COPY channelid.csv channelid.csv
COPY ingestdata.py ingestdata.py

ENTRYPOINT [ "python", "ingestdata.py" ]