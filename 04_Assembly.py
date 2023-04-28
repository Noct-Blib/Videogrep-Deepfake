import pandas as pd
import customPaths
import moviepy
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.editor import *
from videogrep import *
import time



master = pd.read_json(customPaths.masterjs)
querry = pd.DataFrame()
inn = 'what is my blue'
innn = inn.split()
print(innn)
for i in range(len(innn)):
    tmp = master.loc[master["word"] == innn[i]]
    tmp = tmp.sample()
    querry = pd.concat([querry, tmp], ignore_index=True)
print(querry)

videos = customPaths.videos
os.chdir(videos)
clips = []
for index, row in querry.iterrows():
    start, end, video = row['start'], row['end'], row['vpath']
    video = VideoFileClip(video, audio_buffersize=5000).subclip(float(start), float(end))
    # ffmpeg_extract_subclip(row['vpath'], start, end, targetname=customPaths.videoout + "/" + row['vpath'])
    clips.append(video)
    print(round(start), round(end))
    print(row['vpath'])
print("\n")
video = concatenate_videoclips(clips, method="compose")

if os.path.isdir(customPaths.videoout) != True:
    os.mkdir(customPaths.videoout)
os.chdir(customPaths.videoout)

# video.write_videofile("test.mp4", audio=True, audio_bitrate='192k',
#                         audio_fps=44100,
#                         audio_nbytes=2,
#                         audio_codec="aac",
#                         audio_bufsize=1000)#, audio_fps=88200)

video.write_videofile(
        customPaths.videoout+ f"t{time.time()}.mp4",
        codec="libx264",
        temp_audiofile=f"temp-audio{time.time()}.m4a",
        remove_temp=True,
        audio_codec="aac",
    )