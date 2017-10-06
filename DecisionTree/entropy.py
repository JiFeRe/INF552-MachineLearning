from math import log
from collections import Counter



#calculate entropy
def calentropy(label_list):
    listlength = len(label_list)
    entropyset = set(label_list)
    entropy = 0
    for item in entropyset:
        p= label_list.count(item) / listlength
        entropy -= p * log(p, 2)
    return entropy

#splitdata by different value of feature, return splited index set
def splitdata(single_fea):
    single_feaset = set(single_fea)
    split_feaidx = {}
    for item in single_feaset:
        idxset = [idx for idx in range(len(single_fea)) if single_fea[idx] == item]
        split_feaidx.update({item: idxset})
    #print(split_feaidx)
    return split_feaidx

#calculate information gain
def cal_infogain(single_fea,label_list):
    origin_entropy = calentropy(label_list)
    split_feaidx = splitdata(single_fea)
    split_feaset = split_feaidx.keys()
    info_gain = origin_entropy
    for item in split_feaset:
        label_idx = split_feaidx[item]
        split_label = []
        for idx in label_idx:
            split_label.append(label_list[idx])
        info_gain = info_gain - calentropy(split_label)*(len(label_idx)/len(label_list))
    #print(info_gain)
    return info_gain



# choose the best node
def cal_bestnode(leftdata,label_list):
    fea_num = len(leftdata)
    max_gain = -1
    for fea_idx in range(fea_num):
        this_gain = cal_infogain(leftdata[fea_idx],label_list)
        if this_gain > max_gain:
            max_gain = this_gain
            best_node = fea_idx
    #print(best_node)
    return best_node





def creat_tree(fea_namelist, data_list, label_list,times=0):
    cur_times = times
    cur_times += 1
    cur_node = cal_bestnode(data_list, label_list)
    #node_name record
    node_name = fea_namelist[cur_node]
    #print(fea_namelist)
    print('this node is',node_name)
    my_tree = {str(cur_times)+' N '+node_name:{}}
    #how to split
    cur_namelist = fea_namelist[:]
    cur_data = data_list[:]
    split_fea = splitdata(cur_data[cur_node])

    del cur_namelist[cur_node]
    del cur_data[cur_node]
    #root_name record
    for root_name in split_fea:
        root_idx = split_fea[root_name]
        print('this root is',root_name)
        sub_data = []
        sub_label = []
        for sub_idx in root_idx:
            sub_label.append(label_list[sub_idx])
        for attr_idx in range(len(cur_data)):
            sub_attr = []
            for sub_id in root_idx:
                sub_attr.append(cur_data[attr_idx][sub_id])
            sub_data.append(sub_attr)
        #print(sub_data)
        if len(cur_data) == 0:
            out_value = 'tie'
            sublable_set = set(sub_label)
            value_size = 0
            for value_item in sublable_set:
                cur_valuesize=sub_label.count(value_item)
                if cur_valuesize>value_size:
                    out_value=value_item
                    value_size=cur_valuesize
                elif cur_valuesize == value_size:
                    out_value='tie'
            print('end',out_value)
            my_tree[str(cur_times)+' N '+node_name]['Root '+root_name] = out_value
        elif calentropy(sub_label) == 0:
            out_value = ''
            sublable_set = set(sub_label)
            value_size = 0
            for value_item in sublable_set:
                cur_valuesize = sub_label.count(value_item)
                if cur_valuesize > value_size:
                    out_value = value_item
                    value_size = cur_valuesize
                elif cur_valuesize == value_size:
                    out_value = 'tie'
            print('end', out_value)
            my_tree[str(cur_times)+' N '+node_name]['Root '+root_name] = out_value
        else:
            print('continue')
            my_tree[str(cur_times)+' N '+node_name]['Root '+root_name]=creat_tree(cur_namelist,sub_data,sub_label,cur_times)
    return my_tree



