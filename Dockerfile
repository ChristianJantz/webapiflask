FROM ubuntu:16.04

RUN apt-get update && apt-get install -y python python-pip

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY app.py /app/

ENTRYPOINT FLASKAPP=/app/app.py flask run --host=0.0.0.0 --port=8080