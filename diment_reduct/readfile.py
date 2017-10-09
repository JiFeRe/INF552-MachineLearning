import re


def read_points(file_name):
    f = open(file_name)
    point_list = []
    for line in f:
        #no_space = line.rstrip('\n')
        point_list.append([float(line.rstrip('\n').split('\t')[0]),float(line.rstrip('\n').split('\t')[1]),float(line.rstrip('\n').split('\t')[2])])
    #print(point_list)
    return point_list
def read_text(file_name):
    f = open(file_name)
    word_list = []
    for line in f:
        no_space = line.strip('\n')
        word_list.append(no_space)
    # print(point_list)
    return word_list