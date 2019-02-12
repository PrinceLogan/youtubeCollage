#!/usr/bin/python3

import subprocess
import os 
import sys

home = os.path.expanduser("~")
tmpLoc = os.path.join(home, "youtubeCollage", "tmp.txt")
ulDirLoc = "youtube-upload-master/bin/youtube-upload" 
ulDirLocComplete = os.path.join(home, "youtubeCollage", ulDirLoc)

logLoc = os.path.join(home, "youtubeCollage", "log.txt")
sys.stderr = open(logLoc, 'a+')

with open(tmpLoc, 'r') as myfile:
    rando_word=myfile.read().replace('\n', '')

vid1final = rando_word + 'final' + '.mp4'
vid1finalComplete = os.path.join(home, "youtubeCollage", vid1final)

bashVideoArchive = ("python {0}  --title={1}! --description={2}! {3}".format(ulDirLocComplete, rando_word, rando_word, vid1finalComplete))
process1 = subprocess.check_call(bashVideoArchive.split(), stdout=subprocess.PIPE)


