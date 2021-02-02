"""
功能：
将opencv保存下来的无声mp4文件与从原文件提取出来的声音文件相结合

"""

from moviepy.editor import *
import config

if __name__ == '__main__':
    fps = 60
    clip = VideoFileClip(config.tempPath)
    #使用音频与帧表合成视频
    clip.write_videofile(config.resultVideoPath, audio = config.audioSavePath)


