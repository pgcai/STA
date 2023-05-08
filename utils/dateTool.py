'''
获取当前时间方便文件命名

function:
1. getDateYMDHMSU()     返回年月日|时分秒|毫秒
2. getDateYMD()         返回年月日
3. getDateYMDHMS()      返回年月日|时分秒
4. showmissvalue()      返回 缺失的日期
5. leapyear()           判断是否为闰年
6. yeardate()           返回某一年每一个月份有多少天
7. showmissvalue(dirpath) 输出缺失的日期
8. builddateindex(start='', end='') 生成日期索引
'''
import sys
sys.path.append(r'./utils')      # 为了能找到自写函数

import datetime
import os
from dirTool import *


# 返回 年月日 时分秒 毫秒
def getDateYMDHMSU():
    '''
    年月日 时分秒 毫秒
    '''
    now = datetime.datetime.now()
    return now.strftime('%Y%m%d_%H%M%S_%U')

# 返回年月日
def getDateYMD():
    '''
    年月日
    '''
    now = datetime.datetime.now()
    return now.strftime('%Y%m%d')

# 返回 年月日 时分秒
def getDateYMDHMS():
    '''
    年月日
    '''
    now = datetime.datetime.now()
    return now.strftime('%Y%m%d_%H%M%S')

def leapyear(year):
    '''
    判断是否为闰年\n
    input: int(year)
    output: bool(True or False)
    '''
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:return True   # 整百年能被400整除的是闰年
            else:return False
        else:return True       # 非整百年能被4整除的为闰年
    else:return False

def yeardate(year):
    '''
    返回该年份每一月有多少天
    input: int(year)
    output: {1:31, 2:28,...}
    '''
    if leapyear(year):
        return {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    else:
        return {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def showmissvalue(dirpath):
    '''
    返回 缺失的日期\n
    input: dirpath\n
    example:\n
        -test\n
        --2011\n
        ---01\n
        ----01\n
        ...\n
        ----31\n
        ---02\n
        ----01\n
        ...\n
        --2012\n
    output:[*, *, *, ...]
    '''
    missvalue = []

    # 1. 获取年份
    years = subdirname(dirpath)
    for i in years:
        datedic = yeardate(int(i))
        # 2. 获取月份
        monthjudge = subdirname(dirpath + "/" + i)
        # 3. 开始判断日期是否确实
        for j in range(1, 13):
            month = str(j).zfill(2)
            if month not in monthjudge:
                missvalue.append(i+month)    # 月份缺失 添加到缺失值中
                break
            # 4. 获取 day
            dayjudge = subdirname(dirpath + "/" + i + '/' + month)
            # 5. 开始判断日期是否缺失
            for k in range(1, datedic[j]+1):
                day = str(k).zfill(2)
                if day not in dayjudge:
                    missvalue.append(i + month + day)
            # print(day)
            # print(dirpath + i + '/' + month)
    return missvalue

def builddateindex(start='', end=''):
    '''
    Build date index
    生成日期索引
    input example: start='20110101',end='20110103'
    output example:[20110101, 20110102, 20110103]
    '''
    startyear, startmonth, startday= int(start[:4]), int(start[4:6]), int(start[6:])
    endyear, endmonth, endday= int(end[:4]), int(end[4:6]), int(end[6:])
    output = []     # 返回结果
    years = []      # 年份
    for i  in range(endyear-startyear+1):
        years.append(startyear+i)
    for i in years:
        curyear = str(i)
        datedic = yeardate(i)
        print(datedic)
        for j in range(1, 13):
            if i == years[0] and j < startmonth:continue
            if i == years[-1] and j > endmonth:break
            curmonth = str(j).zfill(2)
            for k in range(1, datedic[j]+1):
                if i == years[0] and j == startmonth and k < startday:continue
                if i == years[-1] and j == endmonth and k > endday:break
                curday = str(k).zfill(2)
                output.append(curyear+curmonth+curday)
    return output

def afternday(curdate:str, n:int):
    '''
    n天后的日期
    '''
    startyear, startmonth, startday= int(curdate[:4]), int(curdate[4:6]), int(curdate[6:])
    print(startyear, startmonth, startday)
    i = startyear
    while True:
        curyear = str(i)
        datedic = yeardate(i)
        for j in range(1, 13):
            if i == startyear and j < startmonth:continue
            curmonth = str(j).zfill(2)
            for k in range(1, datedic[j]+1):
                curday = str(k).zfill(2)
                if i == startyear and j == startmonth and k < startday:continue
                print(curyear+curmonth+curday)
                if n-datedic[j]+k-1>0:      # 如果可以直接跳过这个月，则跳过
                    n = n-datedic[j]+k-1
                    break
                if n<=0:return curyear+curmonth+curday
                else:n-=1
        i+=1

def agonday(curdate:str, n:int):
    '''
    n天前的日期
    '''
    startyear, startmonth, startday= int(curdate[:4]), int(curdate[4:6]), int(curdate[6:])
    print(startyear, startmonth, startday)
    i = startyear
    while True:
        curyear = str(i)
        datedic = yeardate(i)
        for j in range(12, 0, -1):
            if i == startyear and j > startmonth:continue
            curmonth = str(j).zfill(2)
            for k in range(datedic[j], 0, -1):
                curday = str(k).zfill(2)
                if i == startyear and j == startmonth and k > startday:continue
                print(curyear+curmonth+curday)
                if n-datedic[j]-k >0:      # 如果可以直接跳过这个月，则跳过
                    n = n-datedic[j]-k
                    break
                if n<=0:return curyear+curmonth+curday
                else:n-=1
        i-=1

