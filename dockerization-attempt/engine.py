#!/usr/bin/python3

import subprocess

event1 = ("./youtubeDL1st.py")
process1 = subprocess.call(event1.split(), stdout=subprocess.PIPE)

event1 = ("./firstTrim2nd.py")
process1 = subprocess.call(event1.split(), stdout=subprocess.PIPE)

event2 = ("./resize3rd.py")
process1 = subprocess.call(event2.split(), stdout=subprocess.PIPE)

event2 = ("./speedAlterVideo4th.py")
process1 = subprocess.call(event2.split(), stdout=subprocess.PIPE)

event2 = ("./filterAudio5th.py")
process1 = subprocess.call(event2.split(), stdout=subprocess.PIPE)

event2 = ("./filterVideo6th.py")
process1 = subprocess.call(event2.split(), stdout=subprocess.PIPE)

event2 = ("./lastTrim7th.py")
process1 = subprocess.call(event2.split(), stdout=subprocess.PIPE)

event2 = ("./finalMerge8th.py")
process1 = subprocess.call(event2.split(), stdout=subprocess.PIPE)

#event2 = ("uploadYoutube9th.py")
#process1 = subprocess.call(event2.split(), stdout=subprocess.PIPE)
         
#event2 = ("cleanup10th.py")
#process1 = subprocess.call(event2.split(), stdout=subprocess.PIPE)

event2 = ("./sftpTest.py")
process1 = subprocess.call(event2.split(), stdout=subprocess.PIPE)

