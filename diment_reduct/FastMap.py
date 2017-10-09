import numpy as np
import readfile
import matplotlib.pyplot as plt

word_list = readfile.read_text('fastmap-wordlist.txt')
raw_points = readfile.read_points('fastmap-data.txt')


def fast_map(point_list):
    # step1: identify the furthest pair
    fur_dist = 0
    for each_pair in point_list:
        if each_pair[2] > fur_dist:
            fur_pair = each_pair
            fur_dist = each_pair[2]
        elif each_pair[2] == fur_dist:
            if (each_pair[0] + each_pair[1]) < (fur_pair[0] + fur_pair[0]):
                fur_pair = each_pair
    #print(fur_pair, fur_dist)

    # step2:
    a = min(fur_pair[0],fur_pair[1])
    b = max(fur_pair[0],fur_pair[1])
    d_ab = fur_dist
    new_pointlist = []
    for each_pair in point_list:
        i = each_pair[0]
        j = each_pair[1]
        d_ij = each_pair[2]
        xi = cal_cord(i, a, b, d_ab)
        xj = cal_cord(j, a, b, d_ab)
        d_ij_new = np.sqrt(d_ij ** 2 - (xi - xj) ** 2)
        new_pointlist.append([i, j, d_ij_new])
    #print(new_pointlist)
    #fast_map(new_pointlist)
    plot_words(new_pointlist, word_list)


def cal_cord(i, a, b, d_ab):
    if i == a:
        first_cord = 0
    elif i == b:
        first_cord = d_ab
    else:
        for each_item in raw_points:
            if each_item[0] == i and each_item[1] == a:
                d_ai = each_item[2]
            if each_item[0] == a and each_item[1] == i:
                d_ai = each_item[2]
            if each_item[0] == i and each_item[1] == b:
                d_bi = each_item[2]
            if each_item[0] == b and each_item[1] == i:
                d_bi = each_item[2]
        first_cord = (d_ai ** 2 + d_ab ** 2 - d_bi ** 2) / (2 * d_ab)
        print(first_cord)
    return first_cord

def plot_words(plot_points, plot_text):
    plt.figure

def main():
    point_list = raw_points[:]
    fast_map(point_list)


main()
