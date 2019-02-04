#!/usr/bin/python3

import os
import subprocess
import time

home = os.path.expanduser("~")
first = os.path.join(home, "youtubeCollage", "youtubeDL1st.py")
second = os.path.join(home, "youtubeCollage", "firstTrim2nd.py")
third = os.path.join(home, "youtubeCollage", "resize3rd.py")
fourth = os.path.join(home, "youtubeCollage", "speedAlterVideo4th.py")
fifth = os.path.join(home, "youtubeCollage", "filterAudio5th.py")
sixth = os.path.join(home, "youtubeCollage", "filterVideo6th.py")
seventh = os.path.join(home, "youtubeCollage", "lastTrim7th.py")
eight = os.path.join(home, "youtubeCollage", "finalMerge8th.py")
nineth = os.path.join(home, "youtubeCollage", "uploadYoutube9th.py")
tenth = os.path.join(home, "youtubeCollage", "cleanup10th.py")


event1 = ("python3 {}".format(first))
process1 = subprocess.call(event1.split(), stdout=subprocess.PIPE)

event1 = ("python3 {}".format(second))
process1 = subprocess.call(event1.split(), stdout=subprocess.PIPE)

event2 = ("python3 {}".format(third))
process1 = subprocess.call(event2.split(), stdout=subprocess.PIPE)

event2 = ("python3 {}".format(fourth))
process1 = subprocess.call(event2.split(), stdout=subprocess.PIPE)

event2 = ("python3 {}".format(fifth))
process1 = subprocess.call(event2.split(), stdout=subprocess.PIPE)

event2 = ("python3 {}".format(sixth))
process1 = subprocess.call(event2.split(), stdout=subprocess.PIPE)

event2 = ("python3 {}".format(seventh))
process1 = subprocess.call(event2.split(), stdout=subprocess.PIPE)

event2 = ("python3 {}".format(eight))
process1 = subprocess.call(event2.split(), stdout=subprocess.PIPE)

event2 = ("python3 {}".format(nineth))
process1 = subprocess.call(event2.split(), stdout=subprocess.PIPE)
         
event2 = ("python3 {}".format(tenth))
process1 = subprocess.call(event2.split(), stdout=subprocess.PIPE)
