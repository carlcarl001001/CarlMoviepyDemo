from moviepy.editor import *
import os
import config
"""
功能：将多个视频合并成一个视频。
用法：可将处理时间过长的视频保存为多个短小视频，避免意外方式导致要重新处理。再将多个小视频用本程序合成一个完整的视频。
"""

def getFileList(path):
    L=[]
    listmv=os.listdir(path)
    print(listmv)
    for each in listmv:
        if os.path.isfile(path+'\\'+each) :
            if each.endswith('.mp4') or each.endswith('.MP4'):
                # print(int(each.strip('.mp4')))
#注意我的文件夹里的视频都是数字+.mp4的!如果不是这种命名格式就修改下面代码！！！！！！！！！！！！！！！！！！！！！！！！！

                L.append(int(each.split('.')[0]))
    L.sort()
    # videofileclip载入视频
    mvFiles=[VideoFileClip(path+'\\'+str(e)+'.mp4') for e in L]
    return mvFiles

if __name__ == '__main__':
    mvTemp=getFileList(config.videoDir)
    final_clip = concatenate_videoclips(mvTemp)
    final_clip.to_videofile('combine.mp4', fps=24, remove_temp=False)