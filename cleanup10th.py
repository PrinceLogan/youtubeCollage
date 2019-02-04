#!/usr/bin/python3

import subprocess
import os

home = os.path.expanduser("~")
tmpLoc = os.path.join(home, "youtubeCollage", "tmp.txt")

with open(tmpLoc, 'r') as myfile:
    rando_word=myfile.read().replace('\n', '')

final = rando_word + 'final' + '.mp4'
finalLoc = os.path.join(home, "youtubeCollage", final)
archLoc = os.path.join(home, "youtubeCollage", "videoArchive", final)

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

bashVideoArchive = ("cp {0} {1}".format(finalLoc,archLoc))
process1 = subprocess.check_call(bashVideoArchive.split(), stdout=subprocess.PIPE)

bashCleanUpVideo1 = ("rm {}".format(vid1output))
bashCleanUpVideo2 = ("rm {}".format(vid2output))
bashCleanUpVideo3 = ("rm {}".format(vid3output))
bashCleanUpVideo4 = ("rm {}".format(vid4output))
bashCleanUpVideo5 = ("rm {}".format(vid5output))
bashCleanUpVideo6 = ("rm {}".format(vid6output))
bashCleanUpVideo7 = ("rm {}".format(finalLoc))

process1 = subprocess.check_call(bashCleanUpVideo1.split(), stdout=subprocess.PIPE)
process2 = subprocess.check_call(bashCleanUpVideo2.split(), stdout=subprocess.PIPE)
process3 = subprocess.check_call(bashCleanUpVideo3.split(), stdout=subprocess.PIPE)
process4 = subprocess.check_call(bashCleanUpVideo4.split(), stdout=subprocess.PIPE)
process5 = subprocess.check_call(bashCleanUpVideo5.split(), stdout=subprocess.PIPE)
process6 = subprocess.check_call(bashCleanUpVideo6.split(), stdout=subprocess.PIPE)
process7 = subprocess.check_call(bashCleanUpVideo7.split(), stdout=subprocess.PIPE)
