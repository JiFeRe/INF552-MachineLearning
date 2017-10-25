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


def perceptron():

    points_cord, points_lable= readfile("classification.txt")

    # record the index and number of misclassified
    def cal_mis(vector):
        mis_idx_list = []
        for i in range(len(points_cord)):
            xi = np.mat(points_cord[i]).T
            yi = points_lable[i]
            constraint = vector.T * xi
            if constraint < 0 and yi == 1:
                mis_idx_list.append(i)
            elif constraint > 0 and yi == -1:
                mis_idx_list.append(i)
        return mis_idx_list

    #step_1 choose w
    ini_sample=random.sample(points_cord,1)
    w = np.mat(ini_sample).T




    #step_2 find violate xi
    a = 0.1
    times = 0
    mis_times = []
    mis_idx_list = cal_mis(w)
    while True:
        mis_nums = len(mis_idx_list)
        print(mis_nums)
        mis_times.append(mis_nums)


        i = random.choice(mis_idx_list)
        xi = np.mat(points_cord[i]).T
        yi = points_lable[i]
        constraint = w.T * xi
        if constraint < 0 and yi == 1:
            cur_w = w + a * xi
            cur_mis = cal_mis(cur_w)
            if len(cur_mis) < mis_nums:
                w = cur_w[:]
                mis_idx_list = cur_mis
        elif constraint > 0 and yi == -1:
            cur_w = w -a * xi
            cur_mis = cal_mis(cur_w)
            if len(cur_mis) < mis_nums:
                w = cur_w[:]
                mis_idx_list = cur_mis
        #print(w)
        if mis_nums == 0 or times >= 7000:
            break
        times += 1
    print(min(mis_times))
    plot_mis(mis_times)
    return min(mis_times)






def plot_mis(numbers):
    plt.figure()
    plt.plot(range(len(numbers)),numbers)
    plt.show()



perceptron()