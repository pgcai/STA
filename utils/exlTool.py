'''
excel读写及特殊操作工具箱

function:
1. read_csv(file_path)  读取csv文件返回列表  
2. read_exl(file_path)  读取excel文件返回列表
3. write2exl(names, wlist, file_path)   将列表写入到excel
4. excel2dict(filepath) 将excel文件装换为字典,键为列名
'''
import csv
import pandas as pd
import numpy as np

# 读取csv文件返回列表
def read_csv(file_path):
    temp=pd.read_csv(file_path, delimiter=',')      # 比numpy的读取方式好太多，真是术业有专攻。
    return temp.values

# 读取excel文件返回列表
def read_exl(file_path):
    data = pd.read_excel(file_path)

    # print(data.head(3))     # 打印前3行数据  
    # print(data['姓名'])     # 根据列名，打印某一列数据  
    # print(data.columns.tolist())    # 查看所有字段
    # print(data.loc[3])          # 只显示第三行
    # print(data[["姓名", "性别"]])       # # 打印多个列数据，需要双层[[]]

    return data.values

def write2exl(names, wlist, file_path):
    '''
    将列表写入到excel
    一条一条数据
    '''
    wlist = np.array(wlist).transpose(1, 0)
    if len(names) != len(wlist):
        print('属性名与属性数不一致！')

    dic = {}
    for i in range(len(names)):
        dic[names[i]] = wlist[i].tolist()
    # print(dic)
    df = pd.DataFrame(dic)
    df.to_excel(file_path)

def excel2dict(filepath):
    '''
    将excel文件装换为字典,键为列名
    input: .xlsx
    output:[{}, {}, {},...]
    '''
    data = pd.read_excel(filepath)
    colnames = data.columns.values
    output = []
    for i in data.values:
        one = {}
        for j in range(len(i)):
            one[colnames[j]] =  i[j]
        output.append(one)
    return output
