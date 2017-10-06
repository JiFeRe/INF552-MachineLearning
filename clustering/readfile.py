# Our group include Zhaoyang Li, Jingfeng Ren and Jiayue Shi

def read_points(file_name):
    x_axis=[]
    y_axis=[]
    all_points = []
    file = open(file_name)
    for line in file:
        no_space = line.rstrip('\n')

        single_point = no_space.split(',')
        float_point = [float(single_point[0]),float(single_point[1])]
        all_points.append(float_point)
        x_axis.append(float_point[0])
        y_axis.append(float_point[1])


    return all_points
