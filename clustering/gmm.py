# Our group include Zhaoyang Li, Jingfeng Ren and Jiayue Shi
import readfile
import random
import numpy as np
import math
import drawgmm


def gmm(pai_list, u_list, sigma_list, last_converge=0, cur_time=0, stop_times=20):
    # e-step
    # nomarlization
    ric_bottomlist = []
    for xi in point_list:
        ric_bottom = 0
        for cc in range(k):
            ric_bottom += pai_list[cc] * gaussian(xi, u_list[cc], sigma_list[cc])
        ric_bottomlist.append(ric_bottom)

    # calculate:ric
    ric_list = []
    for c in range(k):
        single_ric = []
        for i in range(len(point_list)):
            xi = point_list[i]
            ric_top = pai_list[c] * gaussian(xi, u_list[c], sigma_list[c])
            ric = ric_top / (ric_bottomlist[i])
            single_ric.append(ric)
        ric_list.append(single_ric)

    # m-step
    m = len(point_list)
    cur_pai = []
    cur_u = []
    cur_sigma = []
    for c in range(k):
        # calculate mc
        mc = sum(ric_list[c])
        # calculate new amplitude
        cur_pai.append(mc / m)
        # calculate new means
        cur_u_x = 0
        cur_u_y = 0
        for i in range(len(point_list)):
            xi = point_list[i]
            cur_u_x += (ric_list[c][i] * xi[0])
            cur_u_y += (ric_list[c][i] * xi[1])
        single_u = [cur_u_x / mc, cur_u_y / mc]

        # calculate new covariance
        this_mat = np.mat(np.zeros((2, 2)))
        for i in range(len(point_list)):
            xi = point_list[i]
            xi_min_uc = np.mat(xi) - np.mat(single_u)
            this_mat += ric_list[c][i] * xi_min_uc.T * xi_min_uc
        this_mat = this_mat / mc
        single_sigma = this_mat.tolist()

        # append into list
        cur_u.append(single_u)
        cur_sigma.append(single_sigma)

    # calculate convergence
    cur_converge = 0
    for i in range(len(point_list)):
        xi = point_list[i]
        log_convg = 0
        for c in range(k):
            log_convg += cur_pai[c] * gaussian(xi, cur_u[c], cur_sigma[c])
        after_log = math.log(log_convg)
        cur_converge += after_log
    converg_list.append(cur_converge)

    # put into cluster
    cluster_set = []
    for c in range(k):
        cluster_set.append([])
    for i in range(len(point_list)):
        xi = point_list[i]
        max_c = 0
        max_ric = 0
        for c in range(k):
            if ric_list[c][i] > max_ric:
                max_c = c
                max_ric = ric_list[c][i]
        cluster_set[max_c].append(xi)

    # continue or stop？
    # continue
    if cur_time <= 1:
        return gmm(cur_pai, cur_u, cur_sigma, cur_converge, cur_time + 1)
    elif abs(cur_converge - last_converge) >= 0.0001:
        # if cur_time % 10 == 0:
        # print(cur_time)
        # drawgmm.draw_gmm(cur_pai, cur_u, cur_sigma, cluster_set)
        return gmm(cur_pai, cur_u, cur_sigma, cur_converge, cur_time + 1)
    else:
        #stop
        for c in range(k):
            print("Gaussian", c + 1)
            print('mean:', cur_u[c])
            print('amplitude:', cur_pai[c])
            print('covariance matrix:', "\n", np.mat(cur_sigma[c]),'\n')

        drawgmm.draw_log(converg_list)
        drawgmm.draw_gmm(cur_pai, cur_u, cur_sigma, cluster_set)
        return


def gaussian(x, u, sigma):
    sigma_this = np.mat(sigma)
    x_u = np.mat((np.array(x) - np.array(u)))
    x_u_t = x_u.T

    n1 = (1 / ((2 * math.pi) ** (k / 2)))
    n2 = np.linalg.det(sigma_this) ** (-1 / 2)
    n3 = float(x_u * (sigma_this ** (-1)) * x_u_t)
    N = n1 * n2 * math.exp((-1 / 2) * n3)
    result = N
    return result


def initial(k):
    ini_point = all_points[:]
    pai_list = [1 / 3, 1 / 3, 1 / 3]
    u_list = []
    sigma_list = []
    for c in range(k):
        sub_initial = random.sample(ini_point, 4)
        # print(sub_initial)
        uc_x = 0
        uc_y = 0
        # calculate u
        for single_p in sub_initial:
            uc_x += single_p[0] / 4
            uc_y += single_p[1] / 4
        uc = [uc_x, uc_y]
        # calculate sigma
        transfer = []
        for single_p in sub_initial:
            single_sigma = np.array(single_p) - np.array(uc)
            transfer.append(single_sigma.tolist())
            # single_sigma*single_sigma

        sigma_c = (np.mat(transfer).T * np.mat(transfer)) / 4
        # print(sigma_c)
        sigma_list.append(sigma_c.tolist())
        u_list.append(uc)
    return pai_list, u_list, sigma_list

#set parameters
k = 3
converg_list = []
file_name = 'clusters.txt'
all_points = readfile.read_points(file_name)
point_list = all_points[:]
# ini_pai, ini_u, ini_sigma = initial(k)
ini_pai = [1 / 3, 1 / 3, 1 / 3]
ini_u = [random.sample(point_list, 1), random.sample(point_list, 1), random.sample(point_list, 1)]
ini_sigma = [[[0.1, 0.0], [0.0, 0.1]], [[0.1, 0.0], [0.0, 0.1]], [[0.1, 0.0], [0.0, 0.1]]]
print('initial u:', ini_u[0][0], ini_u[1][0], ini_u[2][0])
gmm(ini_pai, ini_u, ini_sigma)
