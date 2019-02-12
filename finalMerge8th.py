#!/usr/bin/python3

import subprocess
import time
import os
import sys

home = os.path.expanduser("~")
tmpLoc = os.path.join(home, "youtubeCollage", "tmp.txt")
listLoc = os.path.join(home, "youtubeCollage", "mylist.txt")

logLoc = os.path.join(home, "youtubeCollage", "log.txt")
sys.stderr = open(logLoc, 'a+')

with open(tmpLoc, 'r') as myfile:
    rando_word=myfile.read().replace('\n', '')

finalName = rando_word + "final.mp4"
finalLoc = os.path.join(home, "youtubeCollage", finalName)

f = open(listLoc, "w")
f.writelines(["file {}00001_Resized.mp4\n".format(rando_word),"file {}00002_Resized.mp4\n".format(rando_word),"file {}00003_Resized.mp4\n".format(rando_word),"file {}00004_Resized.mp4\n".format(rando_word),"file {}00005_Resized.mp4\n".format(rando_word),"file {}00006_Resized.mp4\n".format(rando_word)])
f.close()

finalConcat = ("ffmpeg -f concat -i {0} -c copy {1}".format(listLoc,finalLoc))
process1 = subprocess.check_call(finalConcat.split(), stdout=subprocess.PIPE)
