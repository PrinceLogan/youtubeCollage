#!/usr/bin/python3

import youtube_dl
import subprocess
import os
from CredData import *
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import random
import re
import sys

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
api = tweepy.API(auth)

trends1 = api.trends_place(23424977) # from the end of your code # trends1 is a list with only one element in it, which 
data = trends1[0]
trends = data['trends']
names = [trend['name'] for trend in trends]
random_choixe = random.choice(names)
for k in random_choixe.split("\n"):
    rando_word = re.sub(r"[^a-zA-Z0-9]+", '', k)

x = "ytsearch100:"
y = "%(autonumber)s.%(ext)s"

f = open("tmp.txt", "w")
f.write("{}".format(rando_word))

search = x + rando_word
outputFormat = rando_word + y

ydl_opts = {
    'default_search': '',
    'max_downloads': 3,
    'match_filter': youtube_dl.utils.match_filter_func("duration < 180, duration > 60, width >= 854"),
    'ignoreerrors': True,
    'format': 'mp4',
    'outtmpl': '',
}
ydl_opts["default_search"] = search
ydl_opts["outtmpl"] = outputFormat

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([''])

