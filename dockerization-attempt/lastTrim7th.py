#!/usr/bin/python3
  
import subprocess

with open('tmp.txt', 'r') as myfile:
    rando_word=myfile.read().replace('\n', '')

vid1input = rando_word + '00001' + '_Filtered' + '.mp4'
vid2input = rando_word + '00002' + '_Filtered' + '.mp4'
vid3input = rando_word + '00003' + '_Filtered' + '.mp4'

vid1output = rando_word + '00001' + '_Resized' + '.mp4'
vid2output = rando_word + '00002' + '_Resized' + '.mp4'
vid3output = rando_word + '00003' + '_Resized' + '.mp4'
vid4output = rando_word + '00004' + '_Resized' + '.mp4'
vid5output = rando_word + '00005' + '_Resized' + '.mp4'
vid6output = rando_word + '00006' + '_Resized' + '.mp4'

bashVideoTrim1first = ("ffmpeg -i {0} -ss 00:00:00 -t 00:00:04 -async 1 {1}".format(vid1input,vid1output))
bashVideoTrim2first = ("ffmpeg -i {0} -ss 00:00:00 -t 00:00:09 -async 1 {1}".format(vid3input,vid2output))
bashVideoTrim3first = ("ffmpeg -i {0} -ss 00:00:00 -t 00:00:06 -async 1 {1}".format(vid2input,vid3output))
bashVideoTrim1second = ("ffmpeg -i {0} -ss 00:00:13 -t 00:00:17 -async 1 {1}".format(vid3input,vid4output))
bashVideoTrim2second = ("ffmpeg -i {0} -ss 00:00:13 -t 00:00:17 -async 1 {1}".format(vid2input,vid5output))
bashVideoTrim3second = ("ffmpeg -i {0} -ss 00:00:13 -t 00:00:17 -async 1 {1}".format(vid1input,vid6output))

process1 = subprocess.check_call(bashVideoTrim1first.split(), stdout=subprocess.PIPE)
process2 = subprocess.check_call(bashVideoTrim2first.split(), stdout=subprocess.PIPE)
process3 = subprocess.check_call(bashVideoTrim3first.split(), stdout=subprocess.PIPE)
process4 = subprocess.check_call(bashVideoTrim1second.split(), stdout=subprocess.PIPE)
process5 = subprocess.check_call(bashVideoTrim2second.split(), stdout=subprocess.PIPE)
process6 = subprocess.check_call(bashVideoTrim3second.split(), stdout=subprocess.PIPE)

bashCleanUpTrimVideo1 = ("rm {0}".format(vid1input))
bashCleanUpTrimVideo2 = ("rm {0}".format(vid2input))
bashCleanUpTrimVideo3 = ("rm {0}".format(vid3input))

process1 = subprocess.check_call(bashCleanUpTrimVideo1.split(), stdout=subprocess.PIPE)
process2 = subprocess.check_call(bashCleanUpTrimVideo2.split(), stdout=subprocess.PIPE)
process3 = subprocess.check_call(bashCleanUpTrimVideo3.split(), stdout=subprocess.PIPE)
