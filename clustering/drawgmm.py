# Our group include Zhaoyang Li, Jingfeng Ren and Jiayue Shi
import numpy as np
import matplotlib.pyplot as plt
import math

def draw_gmm(pai_list, u_list, sigma_list,point_list):
    plt.figure()
    X = np.arange(-5,10,0.2)
    Y = np.arange(-5,10,0.2)
    X, Y = np.meshgrid(X,Y)
    colorset = ['black', 'red', 'green', 'blue']
    markerset = ['o','x','+','*']

    point_array = np.array(point_list)
    i = 0

    for c in range(k):
        # plot points in cluster
        x = []
        y = []
        for point in point_array[c]:
            x.append(point[0])
            y.append(point[1])
        plt.scatter(x, y, marker=markerset[c], color=colorset[c], s=25)
        i += 1

        #plot mean
        plt.scatter(u_list[c][0],u_list[c][1], marker=markerset[3], linestyle='dashed',color=colorset[c], s=40)

        #plot Gaussian
        Z = np.array(np.zeros((len(X), len(X[0]))))
        for i in range(len(X)):
            for j in range(len(X[i])):
                Z[i][j] = pai_list[c] * gaussian([X[i][j], Y[i][j]], u_list[c], sigma_list[c])
        plt.contour(X,Y,Z, 5, colors = colorset[c], linewidth = 0.1,)





    plt.show()


def gaussian(x,u,sigma):
    sigma_this  = np.mat(sigma)
    x_u = np.mat((np.array(x)-np.array(u)))
    x_u_t = x_u.T

    n1 = (1/((2*math.pi)**(3/2)))
    n2 = np.linalg.det(sigma_this)**(-1/2)
    n3 = float(x_u*(sigma_this**(-1))*x_u_t)
    N = n1*n2*math.exp((-1/2)*n3)

    result = N
    return result

# draw log-likelihood curve
def draw_log(y):
    x = range(len(y))
    plt.figure()
    plt.plot(x, y, color='black')

k=3