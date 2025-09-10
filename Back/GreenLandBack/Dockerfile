# python version
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE = 1

ENV PYTHONUNBUFFERED = 1

# installing updates
RUN apt-get update && apt-get install -y build-essential && apt-get clean

# choosing work directory
WORKDIR /app

# copying this directory to choosen directory
COPY . /app/

# installing pip update
RUN pip install --upgrade pip

# installing requirements
RUN pip install -r requirements.txt