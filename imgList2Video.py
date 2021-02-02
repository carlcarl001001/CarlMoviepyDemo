"""
注意：
1.生成的new.mp4文件，mac默认到播放器打开会没声音，换个播放器即可。
2.视频帧数小于音频帧数时，这个视频时间会和音频时间一致，视频最后一帧会保持到最后一刻。
"""

import cv2
from moviepy.editor import *
import moviepy.editor as mpy
videoPath=u'/Users/chenxi/my_file/move/snis-731-HD/snis-731-HD.mp4'
videoPath2=u'/Users/chenxi/‎my_file/move/view2.mp4'

cap = cv2.VideoCapture(videoPath)
font = cv2.FONT_HERSHEY_PLAIN
label = videoPath
text_origin=(100,100)
frameIndex=0
frames = []
fps = cap.get(cv2.CAP_PROP_FPS)
print("fps:",fps)
while (True):
    _, frame = cap.read()
    cv2.putText(frame, label, text_origin, font, 2, (0, 255, 0), 1)
    cv2.imshow("frame",frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frames.append(frame)
    #cv2.imshow("result_img",frame) 
    c=cv2.waitKey(1)
    frameIndex =frameIndex + 1
    if (c == 27) or (frameIndex>500):  # esc 
        break

#将图片按帧率(fps)划分，fps可调
clip = ImageSequenceClip(frames, fps = fps)
#使用音频与帧表合成视频
clip.write_videofile('new.mp4', audio = "test.mp3")


