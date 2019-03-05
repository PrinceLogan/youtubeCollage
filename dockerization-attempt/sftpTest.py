#!/usr/bin/python3

import pysftp

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

with open("tmp.txt", 'r') as myfile:
    rando_word=myfile.read().replace('\n', '')

vid1input = rando_word + 'final' + '.mp4'

with pysftp.Connection('23.92.28.207', username='lojoho', password='@cademic12', cnopts=cnopts) as sftp:
    sftp.put("{}".format(vid1input))

