FROM ubuntu:latest
LABEL authors="Thanesh"

# Dockerfile
FROM python:3.11

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y default-libmysqlclient-dev build-essential \
    libjpeg-dev libpng-dev libtiff-dev

RUN groupadd -r django && useradd -r -g django django

COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/

RUN mkdir -p /code/staticfiles /code/media
RUN chown -R django:django /code/staticfiles /code/media
RUN chmod -R 755 /code/staticfiles /code/media

RUN pip install gunicorn

USER django