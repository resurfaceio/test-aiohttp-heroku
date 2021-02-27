FROM python:3.6

WORKDIR /app

ADD . /app

RUN python setup.py develop

EXPOSE 8080