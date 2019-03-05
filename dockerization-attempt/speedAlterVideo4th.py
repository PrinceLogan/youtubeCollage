#!/usr/bin/python3
  
import random
import subprocess

with open('tmp.txt', 'r') as myfile:
    rando_word=myfile.read().replace('\n', '')

vid1output = rando_word + '00001' + '_Resized' + '.mp4'
vid2output = rando_word + '00002' + '_Resized' + '.mp4'
vid3output = rando_word + '00003' + '_Resized' + '.mp4'

vid1Altered = rando_word + '00001' + '_Altered' + '.mp4'
vid2Altered = rando_word + '00002' + '_Altered' + '.mp4'
vid3Altered = rando_word + '00003' + '_Altered' + '.mp4'

def vid_1_fast():
    bashVideoAlter1 = ("ffmpeg -i {0} -filter_complex [0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a] -map [v] -map [a] {1}".format(vid1output,vid1Altered))
    process1 = subprocess.check_call(bashVideoAlter1.split(), stdout=subprocess.PIPE)

def vid_1_slow():
    bashVideoAlter2 = ("ffmpeg -i {0} -filter_complex [0:v]setpts=2.0*PTS[v];[0:a]atempo=0.5[a] -map [v] -map [a] {1}".format(vid1output,vid1Altered))
    process1 = subprocess.check_call(bashVideoAlter2.split(), stdout=subprocess.PIPE)

def vid_1_nothing():
    bashVideoAlter3 = ("cp {0} {1}".format(vid1output,vid1Altered))
    process1 = subprocess.check_call(bashVideoAlter3.split(), stdout=subprocess.PIPE)

def vid_2_fast():
    bashVideoAlter4 = ("ffmpeg -i {0} -filter_complex [0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a] -map [v] -map [a] {1}".format(vid2output,vid2Altered))
    process1 = subprocess.check_call(bashVideoAlter4.split(), stdout=subprocess.PIPE)

def vid_2_slow():
    bashVideoAlter5 = ("ffmpeg -i {0} -filter_complex [0:v]setpts=2.0*PTS[v];[0:a]atempo=0.5[a] -map [v] -map [a] {1}".format(vid2output,vid2Altered))
    process1 = subprocess.check_call(bashVideoAlter5.split(), stdout=subprocess.PIPE)

def vid_2_nothing():
    bashVideoAlter6 = ("cp {0} {1}".format(vid2output,vid2Altered))
    process1 = subprocess.check_call(bashVideoAlter6.split(), stdout=subprocess.PIPE)

def vid_3_fast():
    bashVideoAlter7 = ("ffmpeg -i {0} -filter_complex [0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a] -map [v] -map [a] {1}".format(vid3output,vid3Altered))
    process1 = subprocess.check_call(bashVideoAlter7.split(), stdout=subprocess.PIPE)

def vid_3_slow():
    bashVideoAlter8 = ("ffmpeg -i {0} -filter_complex [0:v]setpts=2.0*PTS[v];[0:a]atempo=0.5[a] -map [v] -map [a] {1}".format(vid3output,vid3Altered))
    process1 = subprocess.check_call(bashVideoAlter8.split(), stdout=subprocess.PIPE)

def vid_3_nothing():
    bashVideoAlter9 = ("cp {0} {1}".format(vid3output,vid3Altered))
    process1 = subprocess.check_call(bashVideoAlter9.split(), stdout=subprocess.PIPE)

list_1 = [vid_1_fast, vid_1_slow, vid_1_nothing]
list_2 = [vid_2_fast, vid_2_slow, vid_2_nothing]
list_3 = [vid_3_fast, vid_3_slow, vid_3_nothing]

random.choice(list_1)()
random.choice(list_2)()
random.choice(list_3)()

bashCleanUpTrimVideo1 = ("rm {0}".format(vid1output))
bashCleanUpTrimVideo2 = ("rm {0}".format(vid2output))
bashCleanUpTrimVideo3 = ("rm {0}".format(vid3output))

process1 = subprocess.check_call(bashCleanUpTrimVideo1.split(), stdout=subprocess.PIPE)
process2 = subprocess.check_call(bashCleanUpTrimVideo2.split(), stdout=subprocess.PIPE)
process3 = subprocess.check_call(bashCleanUpTrimVideo3.split(), stdout=subprocess.PIPE)
