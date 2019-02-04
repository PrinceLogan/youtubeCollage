start_sec = 0
start_effect_sec = 3
end_effect_sec   = 6
end_sec = 60
repeat_p_frames = 15
output_width = 480
fps = 25

output_directory = 'moshed_videos'


		# here's the useful information if you're trying to adapt this into another programming language
		# - convert the video to AVI format
		# - designator for beginning of an i-frame: 0x0001B0
		# - designator for the end of every frame type: 0x30306463 (usually referenced as ASCII 00dc)


# now we get everything set up to make the video file

# import makes other people's code libraries available to use in this code
import sys

# This program was written for Python 3. Python 2 is similar but there are differences and this code won't work with it.
# the argparse code library wasn't included in Python before 3.2 so those previous versions aren't supported.
# If you're stuck with an older version of Python3 you could probably delete all the argparse stuff and it would work 
# but the program would be less convenient to use
if sys.version_info[0] != 3 or sys.version_info[1] < 2:
	print('This version works with Python version 3.2 and above but not Python 2, sorry!')
	sys.exit()

import os
import argparse
import subprocess

# this makes sure the video file exists. It is used below in the 'input_video' argparse
def quit_if_no_video_file(video_file):
	if not os.path.isfile(video_file):
		raise argparse.ArgumentTypeError("Couldn't find {}. You might want to check the file name??".format(video_file))
	else:
		return(video_file)

# make sure the output directory exists
def confirm_output_directory(output_directory):
	if not os.path.exists(output_directory): os.mkdir(output_directory)

	return(output_directory)

# this makes the options available at the command line for ease of use

# 'parser' is the name of our new parser which checks the variables we give it to make sure they will probably work 
# or else offer helpful errors and tips to the user at the command line
parser = argparse.ArgumentParser() 

parser.add_argument('input_video', type=quit_if_no_video_file, help="File to be moshed")
parser.add_argument('--start_sec',        default = start_sec,        type=float, help="Time the video starts on the original footage's timeline. Trims preceding footage.")
parser.add_argument('--end_sec',    	  default = end_sec,          type=float, help="Time on the original footage's time when it is trimmed.")
parser.add_argument('--start_effect_sec', default = start_effect_sec, type=float, help="Time the effect starts on the trimmed footage's timeline. The output video can be much longer.")
parser.add_argument('--end_effect_sec',   default = end_effect_sec,   type=float, help="Time the effect ends on the trimmed footage's timeline.")
parser.add_argument('--repeat_p_frames',  default = repeat_p_frames,  type=int,   help="If this is set to 0 the result will only contain i-frames. Possibly only a single i-frame.")
parser.add_argument('--output_width',     default = output_width,     type=int,   help="Width of output video in pixels. 480 is Twitter-friendly. Programs get real mad if a video is an odd number of pixels wide.")
parser.add_argument('--fps',              default = fps,              type=int,   help="The number of frames per second the initial video is converted to before moshing.")
parser.add_argument('--output_dir',       default = output_directory, type=confirm_output_directory, help="Output directory")

# this makes sure the local variables are up to date after all the argparsing
locals().update( parser.parse_args().__dict__.items() )

# programs get real mad if a video is an odd number of pixels wide (or in height)
if output_width % 2 != 0: output_width += 1

end_effect_hold = end_effect_sec - start_effect_sec
start_effect_sec = start_effect_sec - start_sec

end_effect_sec = start_effect_sec + end_effect_hold

print('start time from original video: ',str(start_sec))
print('end time from original video: ',str(end_sec))
print('mosh effect applied at: ',str(start_effect_sec))
print('mosh effect stops being applied at: ',str(end_effect_sec))

if start_effect_sec > end_effect_sec:
	print("No moshing will occur because --start_effect_sec begins after --end_effect_sec")
	sys.exit()

# where we make new file names
# basename seperates the file name from the directory it's in so /home/user/you/video.mp4 becomes video.mp4
# splitext short for "split extension" splits video.mp4 into a list ['video','.mp4'] and [0] returns 'video' to file_name
file_name = os.path.splitext( os.path.basename(input_video) )[0]
# path.join pushes the directory and file name together and makes sure there's a / between them
input_avi =  os.path.join(output_dir, 'datamoshing_input.avi')			# must be an AVI so i-frames can be located in binary file
output_avi = os.path.join(output_dir, 'datamoshing_output.avi')
# {} is where 'file_name' is put when making the 'output_video' variable
output_video = os.path.join(output_dir, 'moshed_{}.mp4'.format(file_name))		# this ensures we won't over-write your original video


# THIS IS WHERE THE MAGIC HAPPENS

# make sure ffmpeg is installed
try:
	# sends command line output to /dev/null when trying to open ffmpeg so it doesn't muck up our beautiful command line
	null = open("/dev/null", "w")
	# it tries to open ffmpeg
	subprocess.Popen("ffmpeg", stdout=null, stderr=null)
	# politely closes /dev/null
	null.close()

# if the OS can't find ffmpeg an error is printed and the program quits
except OSError:
	print("ffmpeg was not found. Please install it. Thanks.")
	sys.exit()

# convert original file to avi
subprocess.call('ffmpeg -loglevel error -y -i ' + input_video + ' ' +
				' -crf 0 -pix_fmt yuv420p -r ' + str(fps) + ' ' +
				' -ss ' + str(start_sec) + ' -to ' + str(end_sec) + ' ' +
				input_avi, shell=True)

# open up the new files so we can read and write bytes to them
in_file  = open(input_avi,  'rb')
out_file = open(output_avi, 'wb')

# because we used 'rb' above when the file is read the output is in byte format instead of Unicode strings
in_file_bytes = in_file.read()

# 0x30306463 which is ASCII 00dc signals the end of a frame. '0x' is a common way to say that a number is in hexidecimal format.
frames = in_file_bytes.split(bytes.fromhex('30306463'))

# 0x0001B0 signals the beginning of an i-frame. Additional info: 0x0001B6 signals a p-frame
iframe = bytes.fromhex('0001B0')

# We want at least one i-frame before the glitching starts
i_frame_yet = False

for index, frame in enumerate(frames):

	if  i_frame_yet == False or index < int(start_effect_sec * fps) or index > int(end_effect_sec * fps):
		# the split above removed the end of frame signal so we put it back in
		out_file.write(frame + bytes.fromhex('30306463'))

		# found an i-frame, let the glitching begin
		if frame[5:8] == iframe: i_frame_yet = True

	else:
		# while we're moshing we're repeating p-frames and multiplying i-frames
		if frame[5:8] != iframe:
			# this repeats the p-frame x times
			for i in range(repeat_p_frames):
				out_file.write(frame + bytes.fromhex('30306463'))

in_file.close()
out_file.close()
