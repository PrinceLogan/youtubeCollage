FROM ubuntu:16.04

ADD . ./ 

RUN apt-get update
RUN apt-get install -y python3.4 python3-pip
RUN apt-get install -y build-essential libssl-dev libffi-dev python3-dev
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:jonathonf/ffmpeg-4
RUN apt-get -y update
RUN apt-get -y install ffmpeg
RUN apt-get install -y frei0r-plugins 
RUN pip3 install --upgrade youtube_dl
RUN pip3 install tweepy
RUN pip3 install cryptography
RUN pip3 install pysftp

CMD [ "./engine.py" ]
