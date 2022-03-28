# removing duplicated from list using collections.OrderedDict.fromkeys()
# from collections import OrderedDict

# initializing list
from timeit import repeat as rp
from random import shuffle
from collections import Counter

_list = list(range(100000))
_list2 = [13, 43, 13, 14, 13, 13, 16, 3, 4, 5, 4, 3, 3, 56, 43, 5, 5, 5, 5, 5, 5, 12, 13, 14, 15, 3, 4, 56, 4, 3, 4, 4]
shuffle(_list2)
print(_list2)
print(list(set(_list2)))


def dup():
    innalista=[]
    for j in _list:
         if j not in innalista:
              innalista.append(j)
    return innalista

# result_dict = list(dict.fromkeys(_list))
# result_set = list(set(_list))
# no_duplicates = [el for i, el in enumerate(_list) if el not in _list[:i]]
# counter_list = list(Counter(_list))
# print(Counter(_list))


#
# r = 2
# dict_speed = rp("result_dict", number=1, globals=globals(), repeat=r)
# set_speed = rp("result_set", number=1, globals=globals(), repeat=r)
# comp_speed = rp("result_set", number=1, globals=globals(), repeat=r)
# dup_speed = rp("dup()", number=1, globals=globals(), repeat=r)
# counter_speed = rp("counter_list", number=1, globals=globals(), repeat=r)
#
#
# print ("The list after removing duplicates by dict: " + str(sum(dict_speed)/r))
# print ("The list after removing duplicates by set: " + str(sum(set_speed)/r))
# print ("The list after removing duplicates by comp: " + str(sum(comp_speed)/r))
# print ("The list after removing duplicates by dup: " + str(sum(dup_speed)/r))
# print ("The list after removing duplicates by counter: " + str(sum(counter_speed)/r))