# Base image
FROM python:3.6

# Updating repository sources
RUN apt-get update

# Copying requirements.txt file
COPY requirements.txt requirements.txt

# Copying requirements.txt file
COPY demo .

# pip install
RUN pip install --no-cache -r requirements.txt