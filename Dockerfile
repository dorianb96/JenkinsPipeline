# Base image
FROM python:3.6

# Updating repository sources
RUN apt-get update

# Copying requirements.txt file
COPY requirements.txt requirements.txt

# Copying requirements.txt file
COPY src .
COPY test .
COPY test_data .
COPY requirements.txt .

# pip install
RUN pip install --no-cache -r requirements.txt

# install testing requirements
RUN pip install astroid
RUN pip install isort
RUN pip install pylint
RUN pip install pytest
