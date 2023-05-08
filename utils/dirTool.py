'''
获取文件夹下所有图片的路径
author:pgcai
function:
1. get_file(file_path, file_end=('.png', '.jpg', '.jpeg'))      获取指定文件夹下指定后缀文件/不包含子文件夹
2. get_numfile(file_path, file_end=('.png', '.jpg', '.jpeg'))   获取指定文件夹下指定后缀文件/不包含子文件夹//文件名需要为number/排序
3. get_file_sub(file_path, filelist=[], file_end=('.png', '.jpg'))      获取指定文件夹下指定后缀文件/包含子目录
4. get_numfile_sub(file_path, filelist=[], file_end=('.png', '.jpg'))   获取指定文件夹下指定后缀文件/包含子目录/文件名需要为number/排序
5. new_folder(dirpath)  根据当前时间新建文件夹
6. change_suffix(dirpath, file_end=['.png','.jpg'], end_new='')   改变文件夹下指定后缀文件的后缀更改为自定义后缀
7. change_name(dirpath, file_end=['.png','.jpg'], name_add='')    文件名后增加字符串（批量修改文件名）
8. subdirname()     获取一级目录名
'''
import sys
sys.path.append(r'./utils')      # 为了能找到自写函数

import os
import re
from dateTool import *


def check_path(filepath: str) -> None:
    """
    检查地址合法性
    不存在则新建
    :param filepath:地址路径
    :return:None
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

def get_files(folder_path: str, file_extensions: tuple = ('.png', '.jpg', '.jpeg')) -> list:
    '''
    获取指定文件夹下指定后缀文件,不包含子文件夹
    (文件夹路径, 后缀名)
    '''
    file_list = []
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(file_extensions):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                file_list.append(file_path)
    return file_list


def get_numfile(file_path, file_end=('.png', '.jpg', '.jpeg')):
    '''
    获取指定文件夹下指定后缀文件,不包含子文件夹     数字文件排序
    (文件夹路径, 后缀名)
    '''
    filelist = []
    for parent, dirnames, filenames in os.walk(file_path):
        filenames.sort(key=lambda x:int(x[:-4]))  # 按文件名排序 
        for filename in filenames:
            if filename.lower().endswith(file_end):
                filelist.append(os.path.join(parent, filename))
        return filelist



def get_file_sub(file_path, file_end=('.png', '.jpg')):
    '''
    获取指定文件夹下指定后缀文件 包含子目录
    '''
    filelist=[]
    for parent, dirnames, filenames in os.walk(file_path):
        for dirname in dirnames:
            # print(os.path.join(parent, dirname))
            filelist.extend(get_file_sub(os.path.join(parent, dirname), file_end=file_end))
            # print(filelist)
        # print(filenames)
        for filename in filenames:
            if filename.lower().endswith(file_end):
                # print("----------------------------------")
                # print(os.path.join(parent, filename))
                # print("----------------------------------")
                filelist.append(os.path.join(parent, filename))
        return filelist

def get_numfile_sub(file_path, filelist=[], file_end=('.png', '.jpg')):
    '''
    获取指定文件夹下指定后缀文件 包含子目录 文件名需要为 number 便于排序
    '''
    print('\r--------正在统计文件夹下指定后缀文件路径信息--------', end="")
    for parent, dirnames, filenames in os.walk(file_path):
        dirnames.sort() # 按文件夹名排序
        # print("--------------------------------")
        # print(dirnames)
        # print("--------------------------------")
        for dirname in dirnames:
            # print(os.path.join(parent, dirname))
            filelist.extend(get_numfile_sub(os.path.join(parent, dirname), [], file_end=file_end))
            # print(filelist)
            
        # print("old",filenames)
        filenames.sort(key=lambda x:int(x[:-4]))  # 按文件名排序 
        # print("new",filenames)
        for filename in filenames:
            if filename.lower().endswith(file_end):
                # print("----------------------------------")
                # print(os.path.join(parent, filename))
                # print("----------------------------------")
                filelist.append(os.path.join(parent, filename))
        return filelist

def new_folder(dirpath):
    '''
    根据当前时间(年月日时分秒)新建文件夹
    '''
    time_string = getDateYMDHMS()
    makePath =  os.path.join(dirpath, time_string)

    if not os.path.exists(makePath):
        os.makedirs(makePath)
        print("make dir success!")
    else:
        print("folder already exists!")
    return(makePath)


def change_suffix(dirpath, file_end=['.png','.jpg'], end_new=''):
    '''
    改变文件夹下指定后缀文件的后缀更改为自定义后缀
    '''
    for i in file_end:
        print('i = ',i)
        # break
        print(len(i))
        dir_list = get_file(dirpath, i)
        for j in dir_list:
            os.rename(j, j[:-len(i)] + end_new)

def change_name(dirpath, file_end=['.png','.jpg'], name_add=''):
    '''
    文件名后增加字符串（批量修改文件名）
    '''
    for i in file_end:
        print('i = ',i)
        # break
        print(len(i))
        dir_list = get_file(dirpath, i)
        for j in dir_list:
            os.rename(j, j[:-len(i)] + name_add + j[-len(i):])

def subdirname(dirpath):
    """
    返回当前主目录下的所有目录   
    """
    for maindir, subdir, file_name_list in os.walk(dirpath):
        return subdir          






