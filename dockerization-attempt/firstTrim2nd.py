#!/usr/bin/python3

import subprocess
import os
import sys

with open('tmp.txt', 'r') as myfile:
    rando_word=myfile.read().replace('\n', '')

vid1input = rando_word + '00001' + '.mp4'
vid2input = rando_word + '00002' + '.mp4'
vid3input = rando_word + '00003' + '.mp4'

vid1output = rando_word + '00001' + '_FirstTrim' + '.mp4'
vid2output = rando_word + '00002' + '_FirstTrim' + '.mp4'
vid3output = rando_word + '00003' + '_FirstTrim' + '.mp4'

bashVideoTrim1first = ("ffmpeg -i {0} -ss 00:00:00 -t 00:00:45 -async 1 {1}".format(vid1input,vid1output))
bashVideoTrim2first = ("ffmpeg -i {0} -ss 00:00:00 -t 00:00:45 -async 1 {1}".format(vid2input,vid2output))
bashVideoTrim3first = ("ffmpeg -i {0} -ss 00:00:00 -t 00:00:45 -async 1 {1}".format(vid3input,vid3output))

process1 = subprocess.check_call(bashVideoTrim1first.split(), stdout=subprocess.PIPE)
process2 = subprocess.check_call(bashVideoTrim2first.split(), stdout=subprocess.PIPE)
process3 = subprocess.check_call(bashVideoTrim3first.split(), stdout=subprocess.PIPE)

bashCleanUpTrimVideo1 = ("rm {0}".format(vid1input))
bashCleanUpTrimVideo2 = ("rm {0}".format(vid2input))
bashCleanUpTrimVideo3 = ("rm {0}".format(vid3input))

process1 = subprocess.check_call(bashCleanUpTrimVideo1.split(), stdout=subprocess.PIPE)
process2 = subprocess.check_call(bashCleanUpTrimVideo2.split(), stdout=subprocess.PIPE)
process3 = subprocess.check_call(bashCleanUpTrimVideo3.split(), stdout=subprocess.PIPE)
