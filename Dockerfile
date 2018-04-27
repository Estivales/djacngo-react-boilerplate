from python:3.6

MAINTAINER estivaless@gmail.com

# Project Files and Settings
WORKDIR /app/
COPY . /app/

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install