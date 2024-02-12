FROM ubuntu:latest

RUN apt-get update -qy
RUN apt-get install -qy python3.8 python3-pip python3-8-dev
RUN apt-get install -y mongodb

COPY . /studybot
WORKDIR /studybot

RUN pip3 install -r requirements.txt


CMD ["python3", "main.py"]
