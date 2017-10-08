import numpy as np
import readfile


def fast_map():
    point_list = readfile.read_points('fastmap-data.txt')
    # print(point_list)
    # step1: identify the furthest pair
    fur_dist = 0
    for each_pair in point_list:
        if each_pair[2] > fur_dist:
            fur_pair = each_pair
            fur_dist = each_pair[2]
        elif each_pair[2] == fur_dist:
            if (each_pair[0] + each_pair[1]) < (fur_pair[0] + fur_pair[0]):
                fur_pair = each_pair
    print(fur_pair, fur_dist)

    # step2:


fast_map()
