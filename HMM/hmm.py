import numpy as np

def readfile():
    f = open("hmm-data.txt")
    free_num = 0
    level = 0
    cells = []
    observe_all = []
    for line in f:
        if level >= 2 and level <= 11:
            row_x = line.split()
            int_row = list(map(lambda x: int(x), row_x))
            free_num += int_row.count(1)
            cells.append(int_row)

        if level >= 24 and level <= 34:
            observe_t = line.split()
            float_ob = list(map(float, observe_t))
            observe_all.append(float_ob)

        level += 1
    return np.array(cells), np.array(observe_all)


#with one decimal place function
def hmm():
    cells, observe_seq = readfile()
    # initialize for state observe
    init_state = {}
    init_observe = [{}, {}, {}, {}]
    transfer_mat = {}
    for x in range(len(cells)):
        for y in range(len(cells[1])):
            if cells[x][y] != 0:
                # init states for free cell
                init_state[(x, y)] = np.log(1 / 87)
                # init observe
                init_observe[0][(x, y)] = cal_init_observe(0, 0, x, y)
                init_observe[1][(x, y)] = cal_init_observe(0, 9, x, y)
                init_observe[2][(x, y)] = cal_init_observe(9, 0, x, y)
                init_observe[3][(x, y)] = cal_init_observe(9, 9, x, y)
                # init transfer
                neibor_num = 0
                if x - 1 in range(10) and y in range(10):
                    if cells[x - 1][y] != 0:
                        neibor_num += 1
                if x + 1 in range(10) and y in range(10):
                    if cells[x + 1][y] != 0:
                        neibor_num += 1
                if x in range(10) and y - 1 in range(10):
                    if cells[x][y - 1] != 0:
                        neibor_num += 1
                if x in range(10) and y + 1 in range(10):
                    if cells[x][y + 1] != 0:
                        neibor_num += 1
                transfer_mat[(x, y)] = neibor_num

    # print(init_state)
    # print(init_observe)
    # print(transfer_mat)
    # fist step
    sigma_all = []
    delta_all = []
    sigma_1 = {}
    delta_1 = {}
    for free_cell in init_state:
        observe_p = np.log(1)
        for tower in range(4):
            if observe_seq[0][tower] >= init_observe[tower][free_cell][0] and observe_seq[0][tower] <= \
                    init_observe[tower][free_cell][1]:
                observe_p += np.log(1 / init_observe[tower][free_cell][2])
            else:
                observe_p += float("-inf")

        sigma_1[free_cell] = init_state[free_cell] + observe_p
        delta_1[free_cell] = 0
    sigma_all.append(sigma_1)
    #print(sigma_all)
    delta_all.append(delta_1)

    # for t=2-11

    for i in range(1, 11):
        last_sigma = sigma_all[i - 1]
        #print(last_sigma)
        cur_sigma = {}
        cur_delta = {}
        for free_i in init_state:
            max_cur = float("-inf")
            arg_max_j = (0,0)
            for free_j in [(free_i[0] - 1, free_i[1]), (free_i[0], free_i[1] - 1), (free_i[0], free_i[1] + 1),
                           (free_i[0] + 1, free_i[1])]:
                if free_j in last_sigma:
                    #print(np.log((1 / transfer_mat[free_j])),i)
                    j_p = last_sigma[free_j] + np.log((1 / transfer_mat[free_j]))
                    #print(j_p)
                    if j_p > max_cur:
                        #print("find max for", i)
                        max_cur = j_p
                        arg_max_j = free_j

            # calculate observer prob
            observe_p = np.log(1)
            for tower in range(4):
                if observe_seq[i][tower] >= init_observe[tower][free_i][0] and observe_seq[i][tower] <= \
                        init_observe[tower][free_i][1]:
                    observe_p += np.log(1 / init_observe[tower][free_i][2])
                else:
                    observe_p += float("-inf")

            cur_sigma[free_i] = max_cur + observe_p
            cur_delta[free_i] = arg_max_j
        sigma_all.append(cur_sigma)
        delta_all.append(cur_delta)


    #print(sigma_all)
    # start bp
    state_seq = []
    # final round
    max_cell = (0,0)
    cur_sigma = sigma_all[10]
    max_sigma = float("-inf")
    for cell in cur_sigma:
        if cur_sigma[cell] > max_sigma:
            max_sigma = cur_sigma[cell]
            max_cell = cell
        cur_state = max_cell
    state_seq.append(cur_state)

    # previous round
    for i in range(10, 0, -1):
        cur_delta = delta_all[i]
        next_delta = cur_delta[cur_state]
        state_seq.append(next_delta)
        cur_state = next_delta

    state_seq.reverse()
    print("Result with one decimal place probability:")
    print(state_seq)
    print("")






#no one decimal place function
def hmm2():
    cells, observe_seq = readfile()
    # initialize for state observe
    init_state = {}
    init_observe = [{}, {}, {}, {}]
    transfer_mat = {}
    for x in range(len(cells)):
        for y in range(len(cells[1])):
            if cells[x][y] != 0:
                # init states for free cell
                init_state[(x, y)] = np.log(1 / 87)
                # init observe
                init_observe[0][(x, y)] = cal_init_observe(0, 0, x, y)
                init_observe[1][(x, y)] = cal_init_observe(0, 9, x, y)
                init_observe[2][(x, y)] = cal_init_observe(9, 0, x, y)
                init_observe[3][(x, y)] = cal_init_observe(9, 9, x, y)
                # init transfer
                neibor_num = 0
                if x - 1 in range(10) and y in range(10):
                    if cells[x - 1][y] != 0:
                        neibor_num += 1
                if x + 1 in range(10) and y in range(10):
                    if cells[x + 1][y] != 0:
                        neibor_num += 1
                if x in range(10) and y - 1 in range(10):
                    if cells[x][y - 1] != 0:
                        neibor_num += 1
                if x in range(10) and y + 1 in range(10):
                    if cells[x][y + 1] != 0:
                        neibor_num += 1
                transfer_mat[(x, y)] = neibor_num

    # print(init_state)
    # print(init_observe)
    # print(transfer_mat)
    # fist step
    sigma_all = []
    delta_all = []
    sigma_1 = {}
    delta_1 = {}
    for free_cell in init_state:
        observe_p = np.log(1)
        for tower in range(4):
            if observe_seq[0][tower] >= init_observe[tower][free_cell][0] and observe_seq[0][tower] <= \
                    init_observe[tower][free_cell][1]:
                observe_p += np.log(1 / init_observe[tower][free_cell][3])
            else:
                observe_p += float("-inf")

        sigma_1[free_cell] = init_state[free_cell] + observe_p
        delta_1[free_cell] = 0
    sigma_all.append(sigma_1)
    #print(sigma_all)
    delta_all.append(delta_1)

    # for t=2-11

    for i in range(1, 11):
        last_sigma = sigma_all[i - 1]
        #print(last_sigma)
        cur_sigma = {}
        cur_delta = {}
        for free_i in init_state:
            max_cur = float("-inf")
            arg_max_j = (0,0)
            for free_j in [(free_i[0] - 1, free_i[1]), (free_i[0], free_i[1] - 1), (free_i[0], free_i[1] + 1),
                           (free_i[0] + 1, free_i[1])]:
                if free_j in last_sigma:
                    #print(np.log((1 / transfer_mat[free_j])),i)
                    j_p = last_sigma[free_j] + np.log((1 / transfer_mat[free_j]))
                    #print(j_p)
                    if j_p > max_cur:
                        #print("find max for", i)
                        max_cur = j_p
                        arg_max_j = free_j

            # calculate observer prob
            observe_p = np.log(1)
            for tower in range(4):
                if observe_seq[i][tower] >= init_observe[tower][free_i][0] and observe_seq[i][tower] <= \
                        init_observe[tower][free_i][1]:
                    observe_p += np.log(1 / init_observe[tower][free_i][3])
                else:
                    observe_p += float("-inf")

            cur_sigma[free_i] = max_cur + observe_p
            cur_delta[free_i] = arg_max_j
        sigma_all.append(cur_sigma)
        delta_all.append(cur_delta)


    #print(sigma_all)
    # start bp
    state_seq = []
    # final round
    max_cell = (0,0)
    cur_sigma = sigma_all[10]
    max_sigma = float("-inf")
    for cell in cur_sigma:
        if cur_sigma[cell] > max_sigma:
            max_sigma = cur_sigma[cell]
            max_cell = cell
        cur_state = max_cell
    state_seq.append(cur_state)

    # previous round
    for i in range(10, 0, -1):
        cur_delta = delta_all[i]
        next_delta = cur_delta[cur_state]
        state_seq.append(next_delta)
        cur_state = next_delta

    state_seq.reverse()
    #print("Result without one decimal place probability:")
    #print(state_seq)





def cal_init_observe(tower_x, tower_y, cell_x, cell_y):
    dis_left = np.sqrt((cell_x - tower_x) ** 2 + (cell_y - tower_y) ** 2) * 7
    dis_right = np.sqrt((cell_x - tower_x) ** 2 + (cell_y - tower_y) ** 2) * 13
    left = np.ceil(dis_left)
    right = np.floor(dis_right)
    prob = int((right - left) + 1)
    dis_interval = (float('%.1f' % (left / 10)), float("%.1f" % (right / 10)), prob,1)
    return dis_interval



#run hmm
hmm()
hmm2()



