#!/usr/bin/python3

import youtube_dl
from random_word import RandomWords
import subprocess
import os

home = os.path.expanduser("~")
tmpLoc = os.path.join(home, "youtubeCollage", "tmp.txt")

r = RandomWords()
x = "ytsearch100:"
y = "%(autonumber)s.%(ext)s"
rando_word = r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="verb", minCorpusCount=1, maxCorpusCount=10, minDictionaryCount=1, maxDictionaryCount=10, minLength=3, maxLength=6)

f = open(tmpLoc, "w")
f.write("{}".format(rando_word))

search = x + rando_word
outputFormat = rando_word + y

dirLoc = os.path.join(home, "youtubeCollage", outputFormat)

ydl_opts = {
    'default_search': '',
    'max_downloads': 3,
    'match_filter': youtube_dl.utils.match_filter_func("duration < 180, duration > 60, width >= 854"),
    'ignoreerrors': True,
    'format': 'mp4',
    'outtmpl': '',
}
ydl_opts["default_search"] = search
ydl_opts["outtmpl"] = dirLoc

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([''])

