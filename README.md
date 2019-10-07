# youtubeCollage

An automation for generating Youtube content. It relies on [tweepy](http://www.tweepy.org/), [youtube-dl](https://rg3.github.io/youtube-dl/), [ffmpeg](https://www.ffmpeg.org/), & [youtube-upload](https://github.com/tokland/youtube-upload).

Implementation: https://www.youtube.com/channel/UC2JPR7UAdnqxs7Uaezb0WOQ

### engine
Should be the called action when the system is run. Triggers specific actions in sequence.

### youtubeDL1st
Makes a call through tweepy to get a trending phrase from Twitter, and uses this to construct a search through youtube-dl. Three video files are downloaded. Requrires twitter API key. 

### firstTrim2nd
Trims down the downloaded videos to include only the first 45 seconds of each file. 

### resize3rd
Scales all videos to 1280:720. Conformity needed for filters used in the system.  

### speedAlterVideo4th
Each video is either sped up, slowed down, or left alone. The python random function is used to determine which alteration is used on either video. 

### filterAudio5th
Each video is pushed through an audio filter. The python random function is used to determine which audio filter is used on either video. 

### filterVideo6th
Each video is pushed through an video filter. The python random function is used to determine which video filter is used on either video. 

### lastTrim7th
The two videos are cut into 6 parts total, cutting each video into 3 parts. 

### finalMerge8th
The 6 resulting videos are concated back togther in an alternating sequence. 

### uploadYoutube9th
The final product is uploaded to youtube. Requires youtube API key

### cleanup10th
Any of the remaining video pieces are removed, and the final file is moved to an archive directory
