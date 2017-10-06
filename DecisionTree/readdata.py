import re
def readtest():
    read_dt = open('dt-data.txt')
    i = 0
    fea_namelist = []
    rawdata_list = []
    label_list = []
    while True:
        line = read_dt.readline()
        if len(line) == 0:
            break
        else:

            if i == 0:
                no_blank = line.replace(' ', '')
                no_left = no_blank.lstrip('(')
                no_all = no_left.rstrip(')\n')
                split_simple = ','
                all_name = no_all.split(',')
                label_name = all_name[-1]
                fea_namelist = all_name[:-1]
            elif i == 1:
                pass
            else:
                no_blank = line.replace(' ', '')
                no_left = re.sub(r'([\d]+:)', '', no_blank)
                no_all = no_left.rstrip(';\n')
                sglfea_list = no_all.split(',')
                # print(sglfea_list)
                label_list.append(sglfea_list[-1])
                rawdata_list.append(sglfea_list[:-1])
            i += 1
    orig_data = []
    for col_i in range(len(rawdata_list[0])):
        col_list = []
        for row_i in range(len(rawdata_list)):
            col_list.append(rawdata_list[row_i][col_i])
        orig_data.append(col_list)

    #print(label_name,fea_namelist,label_list,orig_data)
    return label_name,fea_namelist,label_list,orig_data

readtest()
