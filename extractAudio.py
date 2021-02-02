from moviepy.editor import *
import config
video = VideoFileClip(config.videoPath)
audio = video.audio
audio.write_audiofile(config.audioSavePath)
print("finish ...")