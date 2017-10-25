import re
import random
import numpy as np
import matplotlib.pyplot as plt

def readfile(file_name):

    cords = []
    labels = []
    f = open(file_name)
    for line in f:
        single_line = line.rstrip("\n").split(",")
        cords.append(list(map(float, single_line[:3])))
        if single_line[4] == "-1":
            labels.append(-1)
        else:
            labels.append(1)
    return cords, labels

def logistic_reg():
    points_cord, points_lable = readfile("classification.txt")

    def cal_ein(vector):
        ein = np.mat(np.zeros(shape=(3,1)))
        n = len(points_lable)
        for i in range(n):
            xi = np.mat(points_cord[i]).T
            yi = points_lable[i]
            mid_value0 = (yi*vector.T*xi)
            mid_value1 = float(mid_value0)
            mid_value2 = np.exp(mid_value1)
            g_value = (1/(1+mid_value2))* yi * xi
            ein += (1/-n)* g_value
        #print(ein)
        return ein


    # step_1 choose w
    ini_sample = random.sample(points_cord, 1)
    w = np.mat(ini_sample).T

    # iteration
    times = 0
    a = 0.1
    while True:
        w= w - a * cal_ein(w)
        times +=1
        if times >= 700:
            print(w)
            return w
            break

logistic_reg()