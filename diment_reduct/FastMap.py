import numpy as np
import readfile
import matplotlib.pyplot as plt

word_list = readfile.read_text('fastmap-wordlist.txt')
raw_points = readfile.read_points('fastmap-data.txt')


def fast_map(point_list):
    # step1: identify the furthest pair
    fur_dist = -1
    for each_pair in point_list:
        if each_pair[2] > fur_dist:
            fur_pair = each_pair
            fur_dist = each_pair[2]
        elif each_pair[2] == fur_dist:
            if (each_pair[0] + each_pair[1]) < (fur_pair[0] + fur_pair[1]):
                fur_pair = each_pair
    #print(fur_pair, fur_dist)


    # step2:
    cord_set = {}
    a = min(fur_pair[0],fur_pair[1])
    b = max(fur_pair[0],fur_pair[1])
    d_ab = fur_dist
    new_pointlist = []
    for each_pair in point_list:
        i = each_pair[0]
        j = each_pair[1]
        d_ij = each_pair[2]

        if i in cord_set:
            xi = cord_set[i]
        else:
            xi = cal_cord(i, a, b, d_ab,point_list)
            cord_set.update({i: xi})

        if j in cord_set:
            xj = cord_set[j]
        else:
            xj = cal_cord(j, a, b, d_ab,point_list)
            cord_set.update({j: xj})

        d_ij_new = np.sqrt(d_ij ** 2 - (xi - xj) ** 2)
        new_pointlist.append([i, j, d_ij_new])
    return cord_set,new_pointlist

def cal_cord(i, a, b, d_ab,point_list):
    if i == a:
        first_cord = 0
    elif i == b:
        first_cord = d_ab
    else:
        for each_item in point_list:
            if each_item[0] == i and each_item[1] == a:
                d_ai = each_item[2]
            if each_item[0] == a and each_item[1] == i:
                d_ai = each_item[2]
            if each_item[0] == i and each_item[1] == b:
                d_bi = each_item[2]
            if each_item[0] == b and each_item[1] == i:
                d_bi = each_item[2]
        first_cord = (d_ai ** 2 + d_ab ** 2 - d_bi ** 2) / (2 * d_ab)
        #print(first_cord)
    return first_cord

def plot_words(cord_1,cord_2, plot_text):
    plt.figure
    plt.scatter(cord_1,cord_2)
    for i in range(len(cord_1)):
        plt.annotate(plot_text[i], xy=(cord_1[i], cord_2[i]))
    #plt.text(cord_1,cord_2,plot_text)
    plt.show()
    plt.close()

def main():
    point_list = raw_points[:]
    cord_1,next_points=fast_map(point_list)
    cord_2=fast_map(next_points)[0]
    print(cord_1)
    print(cord_2)
    plot_words(list(cord_1.values()),list(cord_2.values()),word_list)
    return cord_1,cord_2

main()
