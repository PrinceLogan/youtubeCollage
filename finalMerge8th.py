#!/usr/bin/python3

import subprocess
import time
import os
<<<<<<< HEAD
import sys
=======
>>>>>>> 5403f1439d274e6741ee3947542826e75d7466d9

home = os.path.expanduser("~")
tmpLoc = os.path.join(home, "youtubeCollage", "tmp.txt")
listLoc = os.path.join(home, "youtubeCollage", "mylist.txt")
<<<<<<< HEAD
logLoc = os.path.join(home, "youtubeCollage", "log.txt")

sys.stderr = open(logLoc, 'a+')
=======
>>>>>>> 5403f1439d274e6741ee3947542826e75d7466d9

with open(tmpLoc, 'r') as myfile:
    rando_word=myfile.read().replace('\n', '')

finalName = rando_word + "final.mp4"
finalLoc = os.path.join(home, "youtubeCollage", finalName)

f = open(listLoc, "w")
f.writelines(["file {}00001_Resized.mp4\n".format(rando_word),"file {}00002_Resized.mp4\n".format(rando_word),"file {}00003_Resized.mp4\n".format(rando_word),"file {}00004_Resized.mp4\n".format(rando_word),"file {}00005_Resized.mp4\n".format(rando_word),"file {}00006_Resized.mp4\n".format(rando_word)])
f.close()

finalConcat = ("ffmpeg -f concat -i {0} -c copy {1}".format(listLoc,finalLoc))
process1 = subprocess.check_call(finalConcat.split(), stdout=subprocess.PIPE)
