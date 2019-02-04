#!/usr/bin/python3

import random
import subprocess
import os

home = os.path.expanduser("~")
tmpLoc = os.path.join(home, "youtubeCollage", "tmp.txt")

with open(tmpLoc, 'r') as myfile:
    rando_word=myfile.read().replace('\n', '')

vid1output = rando_word + '00001' + '_Resized' + '.mp4'
vid1outputLoc = os.path.join(home, "youtubeCollage", vid1output)
vid2output = rando_word + '00002' + '_Resized' + '.mp4'
vid2outputLoc = os.path.join(home, "youtubeCollage", vid2output)
vid3output = rando_word + '00003' + '_Resized' + '.mp4'
vid3outputLoc = os.path.join(home, "youtubeCollage", vid3output)

vid1Altered = rando_word + '00001' + '_Altered' + '.mp4'
vid1AlteredLoc = os.path.join(home, "youtubeCollage", vid1Altered)
vid2Altered = rando_word + '00002' + '_Altered' + '.mp4'
vid2AlteredLoc = os.path.join(home, "youtubeCollage", vid2Altered)
vid3Altered = rando_word + '00003' + '_Altered' + '.mp4'
vid3AlteredLoc = os.path.join(home, "youtubeCollage", vid3Altered)

def vid_1_fast():
    bashVideoAlter1 = ("ffmpeg -i {0} -filter_complex [0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a] -map [v] -map [a] {1}".format(vid1outputLoc,vid1AlteredLoc))
    process1 = subprocess.check_call(bashVideoAlter1.split(), stdout=subprocess.PIPE)

def vid_1_slow():
    bashVideoAlter2 = ("ffmpeg -i {0} -filter_complex [0:v]setpts=2.0*PTS[v];[0:a]atempo=0.5[a] -map [v] -map [a] {1}".format(vid1outputLoc,vid1AlteredLoc))
    process1 = subprocess.check_call(bashVideoAlter2.split(), stdout=subprocess.PIPE)

def vid_2_fast():
    bashVideoAlter3 = ("ffmpeg -i {0} -filter_complex [0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a] -map [v] -map [a] {1}".format(vid2outputLoc,vid2AlteredLoc))
    process1 = subprocess.check_call(bashVideoAlter3.split(), stdout=subprocess.PIPE)

def vid_2_slow():
    bashVideoAlter4 = ("ffmpeg -i {0} -filter_complex [0:v]setpts=2.0*PTS[v];[0:a]atempo=0.5[a] -map [v] -map [a] {1}".format(vid2outputLoc,vid2AlteredLoc))
    process1 = subprocess.check_call(bashVideoAlter4.split(), stdout=subprocess.PIPE)

def vid_3_fast():
    bashVideoAlter5 = ("ffmpeg -i {0} -filter_complex [0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a] -map [v] -map [a] {1}".format(vid3outputLoc,vid3AlteredLoc))
    process1 = subprocess.check_call(bashVideoAlter5.split(), stdout=subprocess.PIPE)

def vid_3_slow():
    bashVideoAlter6 = ("ffmpeg -i {0} -filter_complex [0:v]setpts=2.0*PTS[v];[0:a]atempo=0.5[a] -map [v] -map [a] {1}".format(vid3outputLoc,vid3AlteredLoc))
    process1 = subprocess.check_call(bashVideoAlter6.split(), stdout=subprocess.PIPE)

list_1 = [vid_1_fast, vid_1_slow]
list_2 = [vid_2_fast, vid_2_slow]
list_3 = [vid_3_fast, vid_3_slow]

random.choice(list_1)()
random.choice(list_2)()
random.choice(list_3)()

bashCleanUpTrimVideo1 = ("rm {0}".format(vid1outputLoc))
bashCleanUpTrimVideo2 = ("rm {0}".format(vid2outputLoc))
bashCleanUpTrimVideo3 = ("rm {0}".format(vid3outputLoc))

process1 = subprocess.check_call(bashCleanUpTrimVideo1.split(), stdout=subprocess.PIPE)
process2 = subprocess.check_call(bashCleanUpTrimVideo2.split(), stdout=subprocess.PIPE)
process3 = subprocess.check_call(bashCleanUpTrimVideo3.split(), stdout=subprocess.PIPE)
