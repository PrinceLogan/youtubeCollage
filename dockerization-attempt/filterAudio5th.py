#!/usr/bin/python3

import random
import subprocess

with open('tmp.txt', 'r') as myfile:
    rando_word=myfile.read().replace('\n', '')

vid1Altered = rando_word + '00001' + '_Altered' + '.mp4'
vid2Altered = rando_word + '00002' + '_Altered' + '.mp4'
vid3Altered = rando_word + '00003' + '_Altered' + '.mp4'

vid1Filtered = rando_word + '00001' + '_Audio_Filtered' + '.mp4'
vid2Filtered = rando_word + '00002' + '_Audio_Filtered' + '.mp4'
vid3Filtered = rando_word + '00003' + '_Audio_Filtered' + '.mp4'

def echo_1():
    bashVideoAlter1 = ("ffmpeg -i {0} -af aecho=0.8:0.9:1000|500:0.7|0.5 {1}".format(vid1Altered,vid1Filtered))
    process1 = subprocess.check_call(bashVideoAlter1.split(), stdout=subprocess.PIPE)

def tremolo_1():
    bashVideoAlter2 = ("ffmpeg -i {0} -af tremolo=f=10.0:d=0.7 {1}".format(vid1Altered,vid1Filtered))
    process1 = subprocess.check_call(bashVideoAlter2.split(), stdout=subprocess.PIPE)

def vibrato_1():
    bashVideoAlter3 = ("ffmpeg -i {0} -af vibrato=f=7.0:d=0.5 {1}".format(vid1Altered,vid1Filtered))
    process1 = subprocess.check_call(bashVideoAlter3.split(), stdout=subprocess.PIPE)

def chorus_1():
    bashVideoAlter4 = ("ffmpeg -i {0} -af chorus=0.5:0.9:50|60|40:0.4|0.32|0.3:0.25|0.4|0.3:2|2.3|1.3 {1}".format(vid1Altered,vid1Filtered))
    process1 = subprocess.check_call(bashVideoAlter4.split(), stdout=subprocess.PIPE)

def nothing_1():
    bashVideoAlter5 = ("cp {0} {1}".format(vid1Altered,vid1Filtered))
    process1 = subprocess.check_call(bashVideoAlter5.split(), stdout=subprocess.PIPE)

def echo_2():
    bashVideoAlter1 = ("ffmpeg -i {0} -af aecho=0.8:0.9:1000|500:0.7|0.5 {1}".format(vid2Altered,vid2Filtered))
    process1 = subprocess.check_call(bashVideoAlter1.split(), stdout=subprocess.PIPE)

def tremolo_2():
    bashVideoAlter2 = ("ffmpeg -i {0} -af tremolo=f=10.0:d=0.7 {1}".format(vid2Altered,vid2Filtered))
    process1 = subprocess.check_call(bashVideoAlter2.split(), stdout=subprocess.PIPE)

def vibrato_2():
    bashVideoAlter3 = ("ffmpeg -i {0} -af vibrato=f=7.0:d=0.5 {1}".format(vid2Altered,vid2Filtered))
    process1 = subprocess.check_call(bashVideoAlter3.split(), stdout=subprocess.PIPE)

def chorus_2():
    bashVideoAlter4 = ("ffmpeg -i {0} -af chorus=0.5:0.9:50|60|40:0.4|0.32|0.3:0.25|0.4|0.3:2|2.3|1.3 {1}".format(vid2Altered,vid2Filtered))
    process1 = subprocess.check_call(bashVideoAlter4.split(), stdout=subprocess.PIPE)

def nothing_2():
    bashVideoAlter5 = ("cp {0} {1}".format(vid2Altered,vid2Filtered))
    process1 = subprocess.check_call(bashVideoAlter5.split(), stdout=subprocess.PIPE)

def echo_3():
    bashVideoAlter1 = ("ffmpeg -i {0} -af aecho=0.8:0.9:1000|500:0.7|0.5 {1}".format(vid3Altered,vid3Filtered))
    process1 = subprocess.check_call(bashVideoAlter1.split(), stdout=subprocess.PIPE)

def tremolo_3():
    bashVideoAlter2 = ("ffmpeg -i {0} -af tremolo=f=10.0:d=0.7 {1}".format(vid3Altered,vid3Filtered))
    process1 = subprocess.check_call(bashVideoAlter2.split(), stdout=subprocess.PIPE)

def vibrato_3():
    bashVideoAlter3 = ("ffmpeg -i {0} -af vibrato=f=7.0:d=0.5 {1}".format(vid3Altered,vid3Filtered))
    process1 = subprocess.check_call(bashVideoAlter3.split(), stdout=subprocess.PIPE)

def chorus_3():
    bashVideoAlter4 = ("ffmpeg -i {0} -af chorus=0.5:0.9:50|60|40:0.4|0.32|0.3:0.25|0.4|0.3:2|2.3|1.3 {1}".format(vid3Altered,vid3Filtered))
    process1 = subprocess.check_call(bashVideoAlter4.split(), stdout=subprocess.PIPE)

def nothing_3():
    bashVideoAlter5 = ("cp {0} {1}".format(vid3Altered,vid3Filtered))
    process1 = subprocess.check_call(bashVideoAlter5.split(), stdout=subprocess.PIPE)

list_1 = [echo_1, tremolo_1, vibrato_1, chorus_1, nothing_1]
list_2 = [echo_2, tremolo_2, vibrato_2, chorus_2, nothing_2]
list_3 = [echo_3, tremolo_3, vibrato_3, chorus_3, nothing_3]

random.choice(list_1)()
random.choice(list_2)()
random.choice(list_3)()

bashCleanUpTrimVideo1 = ("rm {0}".format(vid1Altered))
bashCleanUpTrimVideo2 = ("rm {0}".format(vid2Altered))
bashCleanUpTrimVideo3 = ("rm {0}".format(vid3Altered))

process1 = subprocess.check_call(bashCleanUpTrimVideo1.split(), stdout=subprocess.PIPE)
process2 = subprocess.check_call(bashCleanUpTrimVideo2.split(), stdout=subprocess.PIPE)
process3 = subprocess.check_call(bashCleanUpTrimVideo3.split(), stdout=subprocess.PIPE)

