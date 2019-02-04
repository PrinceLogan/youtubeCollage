#!/usr/bin/python3

import subprocess
import os
import sys

home = os.path.expanduser("~")
tmpLoc = os.path.join(home, "youtubeCollage", "tmp.txt")
logLoc = os.path.join(home, "youtubeCollage", "log.txt")

sys.stderr = open(logLoc, 'a+')

with open(tmpLoc, 'r') as myfile:
    rando_word=myfile.read().replace('\n', '')

vid1input = rando_word + '00001' + '_FirstTrim' + '.mp4'
vid1inputDir = os.path.join(home, "youtubeCollage", vid1input)
vid2input = rando_word + '00002' + '_FirstTrim' + '.mp4'
vid2inputDir = os.path.join(home, "youtubeCollage", vid2input)
vid3input = rando_word + '00003' + '_FirstTrim' + '.mp4'
vid3inputDir = os.path.join(home, "youtubeCollage", vid3input)

vid1output = rando_word + '00001' + '_Resized' + '.mp4'
vid1outputDir = os.path.join(home, "youtubeCollage", vid1output)
vid2output = rando_word + '00002' + '_Resized' + '.mp4'
vid2outputDir = os.path.join(home, "youtubeCollage", vid2output)
vid3output = rando_word + '00003' + '_Resized' + '.mp4'
vid3outputDir = os.path.join(home, "youtubeCollage", vid3output)

bashVideoResize1 = ("ffmpeg -i {0} -vf scale=1280:720 {1}".format(vid1inputDir,vid1outputDir))
bashVideoResize2 = ("ffmpeg -i {0} -vf scale=1280:720 {1}".format(vid2inputDir,vid2outputDir))
bashVideoResize3 = ("ffmpeg -i {0} -vf scale=1280:720 {1}".format(vid3inputDir,vid3outputDir))

process1 = subprocess.check_call(bashVideoResize1.split(), stdout=subprocess.PIPE)
process2 = subprocess.check_call(bashVideoResize2.split(), stdout=subprocess.PIPE)
process3 = subprocess.check_call(bashVideoResize3.split(), stdout=subprocess.PIPE)

bashCleanUpVideo1 = ("rm {0}".format(vid1inputDir))
bashCleanUpVideo2 = ("rm {0}".format(vid2inputDir))
bashCleanUpVideo3 = ("rm {0}".format(vid3inputDir))

process1 = subprocess.check_call(bashCleanUpVideo1.split(), stdout=subprocess.PIPE)
process2 = subprocess.check_call(bashCleanUpVideo2.split(), stdout=subprocess.PIPE)
process3 = subprocess.check_call(bashCleanUpVideo3.split(), stdout=subprocess.PIPE)
