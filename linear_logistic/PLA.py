import re
import random
import numpy as np

def readfile(file_name):

    cords = []
    labels = []
    f = open(file_name)
    for line in f:
        single_line = line.rstrip("\n").split(",")
        cords.append(list(map(float, single_line[:3])))
        if single_line[3] == "-1":
            labels.append(-1)
        else:
            labels.append(1)
    return cords, labels


def perceptron():
    #read file into list
    points_cord, points_lable = readfile("classification.txt")

    #step_1 choose w
    ini_sample=random.sample(points_cord,1)
    w = np.mat(ini_sample).T


    #step_2 find violate xi
    a = 0.1
    while True:
        no_exist = True
        for i in range(len(points_cord)):
            xi = np.mat(points_cord[i]).T
            yi = points_lable[i]
            constraint = w.T * xi
            if constraint < 0 and yi == 1:
                w = w + a * xi
                no_exist = False
                break
            elif constraint > 0 and yi == -1:
                w = w -a * xi
                no_exist = False
                break
        if no_exist:
            break
    print(w)
    return w

perceptron()

