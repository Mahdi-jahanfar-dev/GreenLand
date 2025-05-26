FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE = 1

ENV PYTHONUNBUFFERED = 1

RUN apt-get update && apt-get install -y build-essential && apt-get clean

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt