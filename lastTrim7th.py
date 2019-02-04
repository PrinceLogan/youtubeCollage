#!/usr/bin/python3

import subprocess
import os

home = os.path.expanduser("~")
tmpLoc = os.path.join(home, "youtubeCollage", "tmp.txt")

with open(tmpLoc, 'r') as myfile:
    rando_word=myfile.read().replace('\n', '')

vid1input = rando_word + '00001' + '_Filtered' + '.mp4'
vid1inputLoc = os.path.join(home, "youtubeCollage", vid1input)
vid2input = rando_word + '00002' + '_Filtered' + '.mp4'
vid2inputLoc = os.path.join(home, "youtubeCollage", vid2input)
vid3input = rando_word + '00003' + '_Filtered' + '.mp4'
vid3inputLoc = os.path.join(home, "youtubeCollage", vid3input)

vid1output = rando_word + '00001' + '_Resized' + '.mp4'
vid1outputLoc = os.path.join(home, "youtubeCollage", vid1output)
vid2output = rando_word + '00002' + '_Resized' + '.mp4'
vid2outputLoc = os.path.join(home, "youtubeCollage", vid2output)
vid3output = rando_word + '00003' + '_Resized' + '.mp4'
vid3outputLoc = os.path.join(home, "youtubeCollage", vid3output)
vid4output = rando_word + '00004' + '_Resized' + '.mp4'
vid4outputLoc = os.path.join(home, "youtubeCollage", vid4output)
vid5output = rando_word + '00005' + '_Resized' + '.mp4'
vid5outputLoc = os.path.join(home, "youtubeCollage", vid5output)
vid6output = rando_word + '00006' + '_Resized' + '.mp4'
vid6outputLoc = os.path.join(home, "youtubeCollage", vid6output)

bashVideoTrim1first = ("ffmpeg -i {0} -ss 00:00:00 -t 00:00:07 -async 1 {1}".format(vid1inputLoc,vid1outputLoc))
bashVideoTrim2first = ("ffmpeg -i {0} -ss 00:00:00 -t 00:00:13 -async 1 {1}".format(vid3inputLoc,vid2outputLoc))
bashVideoTrim3first = ("ffmpeg -i {0} -ss 00:00:00 -t 00:00:09 -async 1 {1}".format(vid2inputLoc,vid3outputLoc))
bashVideoTrim1second = ("ffmpeg -i {0} -ss 00:00:13 -t 00:00:23 -async 1 {1}".format(vid3inputLoc,vid4outputLoc))
bashVideoTrim2second = ("ffmpeg -i {0} -ss 00:00:13 -t 00:00:20 -async 1 {1}".format(vid2inputLoc,vid5outputLoc))
bashVideoTrim3second = ("ffmpeg -i {0} -ss 00:00:13 -t 00:00:23 -async 1 {1}".format(vid1inputLoc,vid6outputLoc))

process1 = subprocess.check_call(bashVideoTrim1first.split(), stdout=subprocess.PIPE)
process2 = subprocess.check_call(bashVideoTrim2first.split(), stdout=subprocess.PIPE)
process3 = subprocess.check_call(bashVideoTrim3first.split(), stdout=subprocess.PIPE)
process4 = subprocess.check_call(bashVideoTrim1second.split(), stdout=subprocess.PIPE)
process5 = subprocess.check_call(bashVideoTrim2second.split(), stdout=subprocess.PIPE)
process6 = subprocess.check_call(bashVideoTrim3second.split(), stdout=subprocess.PIPE)

bashCleanUpTrimVideo1 = ("rm {0}".format(vid1inputLoc))
bashCleanUpTrimVideo2 = ("rm {0}".format(vid2inputLoc))
bashCleanUpTrimVideo3 = ("rm {0}".format(vid3inputLoc))

process1 = subprocess.check_call(bashCleanUpTrimVideo1.split(), stdout=subprocess.PIPE)
process2 = subprocess.check_call(bashCleanUpTrimVideo2.split(), stdout=subprocess.PIPE)
process3 = subprocess.check_call(bashCleanUpTrimVideo3.split(), stdout=subprocess.PIPE)
