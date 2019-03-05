#!/usr/bin/python3

import subprocess

with open('tmp.txt', 'r') as myfile:
    rando_word=myfile.read().replace('\n', '')

vid1input = rando_word + '00001' + '_FirstTrim' + '.mp4'
vid2input = rando_word + '00002' + '_FirstTrim' + '.mp4'
vid3input = rando_word + '00003' + '_FirstTrim' + '.mp4'

vid1output = rando_word + '00001' + '_Resized' + '.mp4'
vid2output = rando_word + '00002' + '_Resized' + '.mp4'
vid3output = rando_word + '00003' + '_Resized' + '.mp4'

bashVideoResize1 = ("ffmpeg -i {0} -vf scale=1280:720 {1}".format(vid1input,vid1output))
bashVideoResize2 = ("ffmpeg -i {0} -vf scale=1280:720 {1}".format(vid2input,vid2output))
bashVideoResize3 = ("ffmpeg -i {0} -vf scale=1280:720 {1}".format(vid3input,vid3output))

process1 = subprocess.check_call(bashVideoResize1.split(), stdout=subprocess.PIPE)
process2 = subprocess.check_call(bashVideoResize2.split(), stdout=subprocess.PIPE)
process3 = subprocess.check_call(bashVideoResize3.split(), stdout=subprocess.PIPE)

bashCleanUpVideo1 = ("rm {0}".format(vid1input))
bashCleanUpVideo2 = ("rm {0}".format(vid2input))
bashCleanUpVideo3 = ("rm {0}".format(vid3input))

process1 = subprocess.check_call(bashCleanUpVideo1.split(), stdout=subprocess.PIPE)
process2 = subprocess.check_call(bashCleanUpVideo2.split(), stdout=subprocess.PIPE)
process3 = subprocess.check_call(bashCleanUpVideo3.split(), stdout=subprocess.PIPE)
