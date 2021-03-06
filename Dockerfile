FROM python:3.7

WORKDIR /app

ADD . /app

RUN python setup.py develop && pip install git+https://github.com/resurfaceio/logger-python@master#egg=usagelogger

EXPOSE 8080