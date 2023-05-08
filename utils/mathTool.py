'''
数学公式库，数学方法库
author:pgcai

function:
1. sigmoid(x)   sigmoid
2. tanh(x)      tanh
3. relu(x)      relu
4. prelu(x, a=0.25)     prelu
5. mean(nlist)  求数组均值
6. var(nlist)   求数组方差
7. std(nlist)   求数组标准差
7. normalization(nlist)     归一化
7.2. normalization_min_numrange(nlist, min, numrange)     指定最小值 范围归一化
8. standardization(nlist)   标准化
9. sta_mean_std(nlist, mean, std)   指定 均值 标准差 标准化
10. euclidean_distance(a, b)        计算两向量的欧氏距离
11. vectorial_resultant(a, b)       计算ab两向量合向量
12. vector_angle(a, b)  计算点a指向点b的矢量 且各维度平方和为1
13. linear_equation_in_2unknowns(a, b, c)   解二元一次方程
14. arctan(theta)   输入正切值，返回角度值
15. arcsin(theta)   输入正弦值，返回角度值
16. arccos(theta)   输入余弦值，返回角度值
17. arc_sin_cos(sin_theta, cos_theta)   同时输入sin 与 cos 计算角度值
18. theta_angle(sin_theta, cos_theta, angle)    输入正弦余弦值，返回旋转angle角度后的正弦余弦值
19. vector_3d_angle(v1, v2)     求两个3-dim向量的夹角
20. rmse(a, b)      RMSE均方误差根
21. mae(a, b)       MAE平均绝对误差
22. cc(a, b)        Correlation coefficient 相关系数
23. 
24. 

'''
import math
import numpy as np

# sigmoid
def sigmoid(x):
    return 1./(1 + np.exp(-x))


# tanh
def tanh(x):
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

# relu
def relu(x):
    return 0 if x<=0 else x

# prelu
def prelu(x, a=0.25):
    return x if x>0 else a*x

def mean(nlist):
    # nlist = np.array(nlist).flatten()
    return np.mean(nlist)

# 方差
def var(nlist):
    return np.var(nlist)

# 标准差
def std(nlist):
    return np.std(nlist)

def normalization(nlist):
    '''
    归一化
    '''
    nlist = np.array(nlist, dtype=np.float32)
    min = np.min(nlist)
    numrange = np.max(nlist) - min

    print("min = ", min)
    print("numrange = ", numrange)

    return (nlist - min) / numrange
def normalization_min_numrange(nlist, min, numrange):
    '''
    指定min, numrange归一化
    '''
    nlist = np.array(nlist, dtype=np.float32)
    return (nlist - min) / numrange

def standardization(nlist):
    '''
    标准化
    '''
    nlist = np.array(nlist, dtype=np.float32)
    mean_list = mean(nlist)
    std_list = std(nlist)
    print("mean_list = ", mean_list)
    print("std_list = ", std_list)
    return (nlist - mean_list) / std_list

def sta_mean_std(nlist, mean, std):
    '''
    标准化\n
    指定 均值 标准差 
    '''
    return (nlist - mean) / std


def euclidean_distance(a, b):
    '''
    计算两向量的欧氏距离
    '''
    if len(a)!=len(b):
        print("please input matrix a, b and len(a)==len(b)")
    vector1 = np.mat(a)
    vector2 = np.mat(b)
    # print (np.sqrt((vector1-vector2)*(vector1-vector2).T))
    return np.asarray(np.sqrt((vector1-vector2)*(vector1-vector2).T))[0][0]


def vectorial_resultant(a, b):
    '''
    计算ab两向量合向量
    '''
    return np.array(b)+np.array(a)


def vector_angle(a, b):
    '''
    计算点位a指向点位b的矢量\n
    且各维度平方和为1
    '''
    c = np.array(b) - np.array(a)
    return c/np.sqrt(np.sum(c*c))

def linear_equation_in_2unknowns(a, b, c):
    '''
    解二元一次方程
    '''
    gen = np.sqrt(b*b - 4*a*c)
    x1 = (-b + gen)/(2.*a)
    x2 = (-b - gen)/(2.*a)
    print(x1, x2)
    return [x1, x2]

def arctan(theta):
    '''
    输入正切值，返回角度值
    '''
    return 180.*math.atan(theta)/math.pi     # 返回角度值

def arcsin(theta):
    '''
    输入正弦值，返回角度值
    '''
    return 180.*math.asin(theta)/math.pi     # 返回角度值

def arccos(theta):
    '''
    输入余弦值，返回角度值
    '''
    return 180.*math.acos(theta)/math.pi     # 返回角度值

def arc_sin_cos(sin_theta, cos_theta):
    '''
    (y,x)
    同时输入sin 与 cos 计算角度值
    '''
    if sin_theta > 0:
        return arccos(cos_theta)
    else:
        return -arccos(cos_theta)

def theta_angle(sin_theta, cos_theta, angle):
    '''
    输入正弦余弦值，返回旋转angle角度后的正弦余弦值
    '''
    _angle = arc_sin_cos(sin_theta, cos_theta)
    angle_now = _angle + angle
    sin_theta2 = math.sin(math.pi*angle_now/180)
    cos_theta2 = math.cos(math.pi*angle_now/180)
    return sin_theta2, cos_theta2

def vector_3d_angle(v1, v2):
    '''
    求两个3-dim向量的夹角
    '''
    v1 = np.array(v1)
    v2 = np.array(v2)
    # print('np.sum(v1*v2) = ', np.sum(v1*v2))
    # print('np.sqrt(np.sum(v1*v1)) = ', np.sqrt(np.sum(v1*v1)))
    # print('np.sqrt(np.sum(v2*v2)) = ', np.sqrt(np.sum(v2*v2)))
    cos_theta = np.sum(v1*v2)/(np.sqrt(np.sum(v1*v1))*np.sqrt(np.sum(v2*v2)))
    print(cos_theta)
    return arccos(cos_theta)

def rmse(a, b):
    '''
    求两数组的RMSE均方根误差\n
    a:真实值    b:预测值
    '''
    a, b = np.array(a), np.array(b)
    c = b - a
    m = len(a)
    return np.sqrt(np.sum(c*c)/m)

def mae(a, b):
    '''
    求两数组的MAE平均绝对误差\n
    a:真实值    b:预测值
    '''
    a, b = np.array(a), np.array(b)
    c = np.absolute(b - a)
    m = len(a)
    return np.sum(c)/m

def cc(a, b):
    '''
    Correlation coefficient 相关系数\n
    a:真实值    b:预测值
    '''    
    a, b = np.array(a), np.array(b)
    mean_a = mean(a)
    mean_b = mean(b)
    print(mean_a, mean_b)
    
    up = np.sum((a - mean_a)*(b - mean_b))
    down = math.sqrt(np.sum((a - mean_a)**2 )) * math.sqrt(np.sum((b - mean_b)**2))
    return up/down
    # return np.corrcoef(a, b)
    


