'''
视频工具箱
包含功能：

author：pgcai

function:
1. def video2img(videoPath, savePath, timeF = 1, file_end='.jpg')   将视频分帧到指定文件夹
2. img2video(savePath, videoPath, fps = 30, file_end=('.jpg'))  将指定文件夹图片合成为视频
3. 拼接两个视频
4. 

'''
import sys
sys.path.append('./')
import cv2
import os
from dirTool import get_files, get_numfile
import numpy as np


# 将视频分帧到指定文件夹
# (,,视频帧计数间隔频率)
def video2img(videoPath, savePath, timeF = 1, file_end='.jpg'):
    print("video2img ing ******")
    vc = cv2.VideoCapture(videoPath)  # 读入视频文件，命名cv
    n = 0   # 计数 已读取帧数
    i = 0   # 计数 已保存帧数

    # 判断是否正常打开
    if vc.isOpened(): rval, frame = vc.read()
    else: rval = False
    
    while rval:  # 循环读取视频帧
        if (n % timeF == 0):  # 每隔timeF帧进行存储操作
            i += 1
            print('\r已保存帧数 '+str(i), end='')
            # if i>4500:
            cv2.imwrite(savePath + r'/{}'.format(i) + file_end, frame)  # 存储为图像
        n = n + 1
        cv2.waitKey(1)
        rval, frame = vc.read()
    vc.release()
    print("\nvideo2img success!!!")



# 将指定文件夹图片合成为视频
def img2video(savePath, videoPath, fps = 30, file_end=('.jpg'), file_name_num=False):
    print("img2video ing ******")
    # imglist = get_numfile(savePath, file_end)
    if file_name_num:
        imglist = get_numfile(savePath, file_end)
    else:
        imglist = get_files(savePath, file_end)
    print(imglist)
    img = cv2.imread(imglist[0])  #读取第一张图片
    print("imglist[0] = ",imglist[0])
    print(img)
    img = np.array(img)
    print("img.shape = ", img.shape)
    imgInfo = img.shape
    size = (imgInfo[1],imgInfo[0])  #获取图片宽高度信息
    print(size)
    fourcc = cv2.VideoWriter_fourcc('X','2','6','4')
    videoWrite = cv2.VideoWriter(videoPath + 'output.mp4',fourcc,fps,size)# 根据图片的大小，创建写入对象 （文件名，支持的编码器，5帧，视频大小（图片大小））
    #videoWrite = cv2.VideoWriter('0.mp4',fourcc,fps,(1920,1080))

    for i in imglist:
        img = cv2.imread(i)
        print('\r视频已加入帧 '+i, end='')
        videoWrite.write(img)# 将图片写入所创建的视频对象
    print("\nimg2video success!!!")

def zkhy_pre(img):
    left = img[:1184]
    disp = img[1200:]
    img2 = np.hstack((left, disp))
    return img2
# 将指定文件夹图片合成为视频
def img2video_zkhy(savePath, videoPath, fps = 30, file_end=('.jpg')):
    print("img2video ing ******")
    # imglist = get_numfile(savePath, file_end)
    # imglist = get_numfile(savePath, file_end)
    imglist = get_files(savePath, file_end)
    print(imglist)
    img = cv2.imread(imglist[0])  #读取第一张图片
    print("imglist[0] = ",imglist[0])
    print(img)
    img = zkhy_pre(img)
    img = np.array(img)
    print("img.shape = ", img.shape)
    imgInfo = img.shape
    size = (imgInfo[1],imgInfo[0])  #获取图片宽高度信息
    print(size)
    fourcc = cv2.VideoWriter_fourcc('X','2','6','4')
    videoWrite = cv2.VideoWriter(videoPath + 'output.mp4', fourcc, fps, size)# 根据图片的大小，创建写入对象 （文件名，支持的编码器，5帧，视频大小（图片大小））
    #videoWrite = cv2.VideoWriter('0.mp4',fourcc,fps,(1920,1080))

    for i in imglist:
        img = cv2.imread(i)
        img = zkhy_pre(img)
        print('\r视频已加入帧 '+i, end='')
        videoWrite.write(img)# 将图片写入所创建的视频对象
    print("\nimg2video success!!!")


def concatenate_videos(input_videos, output_path):
    """
    将多个MP4视频拼接成一个视频

    参数：
    input_videos：一个包含所有输入视频文件路径的列表
    output_path：输出视频文件路径

    返回值：
    无
    """
    from moviepy.editor import VideoFileClip, concatenate_videoclips
    clips = []
    # 遍历所有输入视频文件，并将它们添加到clips列表中
    for video_path in input_videos:
        clip = VideoFileClip(video_path)
        clips.append(clip)

    # 拼接所有clips并写入输出文件
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_path)



