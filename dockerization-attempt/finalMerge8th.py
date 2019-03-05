#!/usr/bin/python3

import subprocess
import time

with open('tmp.txt', 'r') as myfile:
    rando_word=myfile.read().replace('\n', '')

finalName = rando_word + "final.mp4"

f = open('list.txt', "w")
f.writelines(["file {}00001_Resized.mp4\n".format(rando_word),"file {}00002_Resized.mp4\n".format(rando_word),"file {}00003_Resized.mp4\n".format(rando_word),"file {}00004_Resized.mp4\n".format(rando_word),"file {}00005_Resized.mp4\n".format(rando_word),"file {}00006_Resized.mp4\n".format(rando_word)])
f.close()

finalConcat = ("ffmpeg -f concat -i {0} -c copy {1}".format('list.txt',finalName))
process1 = subprocess.check_call(finalConcat.split(), stdout=subprocess.PIPE)
