import numpy as np
import readfile

def cal_pca(n=3,k=2):
    point_list = readfile.read_points()
    point_mat = np.mat(point_list)
    #step 1
    sigma = point_mat.T * point_mat
    #print(sigma)

    #step 2
    e_value,e_vector = np.linalg.eig(sigma)
    #step 3 ??
    u_nn = e_vector[:]
    u_kn = u_nn[:k]
    #step 4
    z_list = []
    for i in range(len(point_list)):
        xi = point_list[i]
        xi_mat = np.mat(xi).T
        zi = u_kn * xi_mat
        z_list.append(zi.T.tolist())
    print(z_list)

cal_pca()