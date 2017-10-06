import matplotlib.pyplot as plt
import numpy as np


def drawcluster(point_list):
    point_array = np.array(point_list)
    # print(len(point_array))
    i = 0
    plt.figure()
    for cluster in point_array:

        x = []
        y = []
        for point in cluster:
            x.append(point[0])
            y.append(point[1])
        colorset = ['black', 'red', 'green', 'blue']
        plt.scatter(x, y, color=colorset[i], s=10)
        i += 1
    plt.show()
