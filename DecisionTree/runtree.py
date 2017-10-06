import entropy
import readdata
label_name, fea_namelist,label_list,orig_data = readdata.readtest()
#fea_namelist = ['weather', 'food']
#orig_data = [['s', 'w', 's', 'w'], ['a', 'c','c', 'c']]
#label_list = ['y', 'y', 'n', 'n']
Mytree = entropy.creat_tree(fea_namelist,orig_data,label_list)
print(Mytree)
