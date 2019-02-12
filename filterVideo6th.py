#!/usr/bin/python3

import random
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

vid1Altered = rando_word + '00001' + '_Audio_Filtered' + '.mp4'
vid1AlteredLoc = os.path.join(home, "youtubeCollage", vid1Altered)
vid2Altered = rando_word + '00002' + '_Audio_Filtered' + '.mp4'
vid2AlteredLoc = os.path.join(home, "youtubeCollage", vid2Altered)
vid3Altered = rando_word + '00003' + '_Audio_Filtered' + '.mp4'
vid3AlteredLoc = os.path.join(home, "youtubeCollage", vid3Altered)

vid1Filtered = rando_word + '00001' + '_Filtered' + '.mp4'
vid1FilteredLoc = os.path.join(home, "youtubeCollage", vid1Filtered)
vid2Filtered = rando_word + '00002' + '_Filtered' + '.mp4'
vid2FilteredLoc = os.path.join(home, "youtubeCollage", vid2Filtered)
vid3Filtered = rando_word + '00003' + '_Filtered' + '.mp4'
vid3FilteredLoc = os.path.join(home, "youtubeCollage", vid3Filtered)

def vertigo_1():
    bashVideoAlter1 = ("ffmpeg -i {0} -vf frei0r=vertigo:0.2 {1}".format(vid1AlteredLoc,vid1FilteredLoc))
    process1 = subprocess.check_call(bashVideoAlter1.split(), stdout=subprocess.PIPE)

def distorted_1():
    bashVideoAlter2 = ("ffmpeg -i {0} -vf frei0r=distort0r:0.05|0.0000001 {1}".format(vid1AlteredLoc,vid1FilteredLoc))
    process1 = subprocess.check_call(bashVideoAlter2.split(), stdout=subprocess.PIPE)

def nervous_1():
    bashVideoAlter3 = ("ffmpeg -i {0} -vf frei0r=nervous {1}".format(vid1AlteredLoc,vid1FilteredLoc))
    process1 = subprocess.check_call(bashVideoAlter3.split(), stdout=subprocess.PIPE)

def roxxor_1():
    bashVideoAlter4 = ("ffmpeg -i {0} -vf frei0r=tehroxx0r {1}".format(vid1AlteredLoc,vid1FilteredLoc))
    process1 = subprocess.check_call(bashVideoAlter4.split(), stdout=subprocess.PIPE)

def twoplayer_1():
    bashVideoAlter5 = ("ffmpeg -i {0} -vf frei0r=twolay0r {1}".format(vid1AlteredLoc,vid1FilteredLoc))
    process1 = subprocess.check_call(bashVideoAlter5.split(), stdout=subprocess.PIPE)

def invertor_1():
    bashVideoAlter6 = ("ffmpeg -i {0} -vf frei0r=invert0r {1}".format(vid1AlteredLoc,vid1FilteredLoc))
    process1 = subprocess.check_call(bashVideoAlter6.split(), stdout=subprocess.PIPE)

def nothing_1():
    bashVideoAlter7 = ("cp {0} {1}".format(vid1AlteredLoc,vid1FilteredLoc))
    process1 = subprocess.check_call(bashVideoAlter7.split(), stdout=subprocess.PIPE)

def vertigo_2():
    bashVideoAlter1 = ("ffmpeg -i {0} -vf frei0r=vertigo:0.2 {1}".format(vid2AlteredLoc,vid2FilteredLoc))
    process1 = subprocess.check_call(bashVideoAlter1.split(), stdout=subprocess.PIPE)

def distorted_2():
    bashVideoAlter2 = ("ffmpeg -i {0} -vf frei0r=distort0r:0.05|0.0000001 {1}".format(vid2AlteredLoc,vid2FilteredLoc))
    process1 = subprocess.check_call(bashVideoAlter2.split(), stdout=subprocess.PIPE)

def nervous_2():
    bashVideoAlter3 = ("ffmpeg -i {0} -vf frei0r=nervous {1}".format(vid2AlteredLoc,vid2FilteredLoc))
    process1 = subprocess.check_call(bashVideoAlter3.split(), stdout=subprocess.PIPE)

def roxxor_2():
    bashVideoAlter4 = ("ffmpeg -i {0} -vf frei0r=tehroxx0r {1}".format(vid2AlteredLoc,vid2FilteredLoc))
    process1 = subprocess.check_call(bashVideoAlter4.split(), stdout=subprocess.PIPE)

def twoplayer_2():
    bashVideoAlter5 = ("ffmpeg -i {0} -vf frei0r=twolay0r {1}".format(vid2AlteredLoc,vid2FilteredLoc))
    process1 = subprocess.check_call(bashVideoAlter5.split(), stdout=subprocess.PIPE)

def invertor_2():
    bashVideoAlter6 = ("ffmpeg -i {0} -vf frei0r=invert0r {1}".format(vid2AlteredLoc,vid2FilteredLoc))
    process1 = subprocess.check_call(bashVideoAlter6.split(), stdout=subprocess.PIPE)

def nothing_2():
    bashVideoAlter7 = ("cp {0} {1}".format(vid2AlteredLoc,vid2FilteredLoc))
    process1 = subprocess.check_call(bashVideoAlter7.split(), stdout=subprocess.PIPE)

def vertigo_3():
    bashVideoAlter1 = ("ffmpeg -i {0} -vf frei0r=vertigo:0.2 {1}".format(vid3AlteredLoc,vid3FilteredLoc))
    process1 = subprocess.check_call(bashVideoAlter1.split(), stdout=subprocess.PIPE)

def distorted_3():
    bashVideoAlter2 = ("ffmpeg -i {0} -vf frei0r=distort0r:0.05|0.0000001 {1}".format(vid3AlteredLoc,vid3FilteredLoc))
    process1 = subprocess.check_call(bashVideoAlter2.split(), stdout=subprocess.PIPE)

def nervous_3():
    bashVideoAlter3 = ("ffmpeg -i {0} -vf frei0r=nervous {1}".format(vid3AlteredLoc,vid3FilteredLoc))
    process1 = subprocess.check_call(bashVideoAlter3.split(), stdout=subprocess.PIPE)

def roxxor_3():
    bashVideoAlter4 = ("ffmpeg -i {0} -vf frei0r=tehroxx0r {1}".format(vid3AlteredLoc,vid3FilteredLoc))
    process1 = subprocess.check_call(bashVideoAlter4.split(), stdout=subprocess.PIPE)

def twoplayer_3():
    bashVideoAlter5 = ("ffmpeg -i {0} -vf frei0r=twolay0r {1}".format(vid3AlteredLoc,vid3FilteredLoc))
    process1 = subprocess.check_call(bashVideoAlter5.split(), stdout=subprocess.PIPE)

def invertor_3():
    bashVideoAlter6 = ("ffmpeg -i {0} -vf frei0r=invert0r {1}".format(vid3AlteredLoc,vid3FilteredLoc))
    process1 = subprocess.check_call(bashVideoAlter6.split(), stdout=subprocess.PIPE)

def nothing_3():
    bashVideoAlter7 = ("cp {0} {1}".format(vid3AlteredLoc,vid3FilteredLoc))
    process1 = subprocess.check_call(bashVideoAlter7.split(), stdout=subprocess.PIPE)

list_1 = [vertigo_1, distorted_1, nervous_1, roxxor_1, twoplayer_1, invertor_1, nothing_1]
list_2 = [vertigo_2, distorted_2, nervous_2, roxxor_2, twoplayer_2, invertor_2, nothing_2]
list_3 = [vertigo_3, distorted_3, nervous_3, roxxor_3, twoplayer_3, invertor_3, nothing_3]

random.choice(list_1)()
random.choice(list_2)()
random.choice(list_3)()

bashCleanUpTrimVideo1 = ("rm {0}".format(vid1AlteredLoc))
bashCleanUpTrimVideo2 = ("rm {0}".format(vid2AlteredLoc))
bashCleanUpTrimVideo3 = ("rm {0}".format(vid3AlteredLoc))

process1 = subprocess.check_call(bashCleanUpTrimVideo1.split(), stdout=subprocess.PIPE)
process2 = subprocess.check_call(bashCleanUpTrimVideo2.split(), stdout=subprocess.PIPE)
process3 = subprocess.check_call(bashCleanUpTrimVideo3.split(), stdout=subprocess.PIPE)

