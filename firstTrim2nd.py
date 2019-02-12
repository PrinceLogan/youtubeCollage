#!/usr/bin/python3

import subprocess
import os
import sys

home = os.path.expanduser("~")
tmpLoc = os.path.join(home, "youtubeCollage", "tmp.txt")
logLoc = os.path.join(home, "youtubeCollage", "log.txt")

sys.stderr = open(logLoc, 'a+')
home = os.path.expanduser("~")
tmpLoc = os.path.join(home, "youtubeCollage", "tmp.txt")

with open(tmpLoc, 'r') as myfile:
    rando_word=myfile.read().replace('\n', '')

vid1input = rando_word + '00001' + '.mp4'
vid1inputLoc = os.path.join(home, "youtubeCollage", vid1input)
vid2input = rando_word + '00002' + '.mp4'
vid2inputLoc = os.path.join(home, "youtubeCollage", vid2input)
vid3input = rando_word + '00003' + '.mp4'
vid3inputLoc = os.path.join(home, "youtubeCollage", vid3input)

vid1output = rando_word + '00001' + '_FirstTrim' + '.mp4'
vid1outputLoc = os.path.join(home, "youtubeCollage", vid1output)
vid2output = rando_word + '00002' + '_FirstTrim' + '.mp4'
vid2outputLoc = os.path.join(home, "youtubeCollage", vid2output)
vid3output = rando_word + '00003' + '_FirstTrim' + '.mp4'
vid3outputLoc = os.path.join(home, "youtubeCollage", vid3output)

bashVideoTrim1first = ("ffmpeg -i {0} -ss 00:00:00 -t 00:00:45 -async 1 {1}".format(vid1inputLoc,vid1outputLoc))
bashVideoTrim2first = ("ffmpeg -i {0} -ss 00:00:00 -t 00:00:45 -async 1 {1}".format(vid2inputLoc,vid2outputLoc))
bashVideoTrim3first = ("ffmpeg -i {0} -ss 00:00:00 -t 00:00:45 -async 1 {1}".format(vid3inputLoc,vid3outputLoc))

process1 = subprocess.check_call(bashVideoTrim1first.split(), stdout=subprocess.PIPE)
process2 = subprocess.check_call(bashVideoTrim2first.split(), stdout=subprocess.PIPE)
process3 = subprocess.check_call(bashVideoTrim3first.split(), stdout=subprocess.PIPE)

bashCleanUpTrimVideo1 = ("rm {0}".format(vid1inputLoc))
bashCleanUpTrimVideo2 = ("rm {0}".format(vid2inputLoc))
bashCleanUpTrimVideo3 = ("rm {0}".format(vid3inputLoc))

process1 = subprocess.check_call(bashCleanUpTrimVideo1.split(), stdout=subprocess.PIPE)
process2 = subprocess.check_call(bashCleanUpTrimVideo2.split(), stdout=subprocess.PIPE)
process3 = subprocess.check_call(bashCleanUpTrimVideo3.split(), stdout=subprocess.PIPE)
