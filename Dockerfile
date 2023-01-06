# https://github.com/testdrivenio/fastapi-docker-traefik/blob/master/Dockerfile.prod

FROM python:3.11

RUN apt-get update && apt-get install -y netcat

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .