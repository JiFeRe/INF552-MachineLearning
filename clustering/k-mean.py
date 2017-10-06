import random
import readfile
import drawcluster

def kmean(u_list,cur_time = 0,stop_times=50):
    #points_list = all_points[:]
    #assignment
    sc = []
    for c in range(k):
        s = []
        sc.append(s)
    #print(sc)
    for single_point in points_list:
        dis_list = []
        for uc in u_list:
            dist = 0
            for (x,y) in zip(single_point, uc):
                dist +=(x-y)**2
            dis_list.append(dist)
        zi = dis_list.index(min(dis_list))
        #print(zi)
        sc[zi].append(single_point)
    #print(sc)



    #recomputation
    center_u = []
    for c in range(k):
        mc = len(sc[c])
        if mc == 0:
            center_u.append(u_list[c])
        else:
            sum_x = 0
            sum_y = 0
            for i in range(len(sc[c])):
                # print(i)
                sum_x += sc[c][i][0]
                sum_y += sc[c][i][1]
            sum_c = [sum_x / mc, sum_y / mc]
            center_u.append(sum_c)
    #print(center_u)


    #next iterat
    cur_time += 1
    if center_u == u_list:
        # if cur_time%5==0:
        #     #print(cur_time)
        #     drawcluster.drawcluster(sc)
        #     print('continue')
        print(center_u)
        print(cur_time)
        drawcluster.drawcluster(sc)
        return
    elif cur_time >= stop_times:
        print(center_u)
        drawcluster.drawcluster(sc)
        return
    else:
        return kmean(center_u, cur_time)




def initialize(k):
    u_list = []
    for c in range(k):
        random_x = random.uniform(-4.260793979, 9.24625283)
        random_y = random.uniform(-3.530784753, 8.595480962)
        uc=[random_x,random_y]
        u_list.append(uc)
    #print(u_list)
    return u_list

k = 3
file_name = 'clusters.txt'
initial_u = initialize(k)
#initial_u = [[-4.260793979, 8.595480962],[9.24625283, -3.530784753],[-4, 8]]
#print('init',initial_u)
all_points = readfile.read_points(file_name)
points_list = all_points[:]
kmean(initial_u)

