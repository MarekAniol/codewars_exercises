# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
#
# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []
#
# You can assume that all values are integers. Do not mutate the input array/list.
import numpy as np

def invert_np(lst):
    lst = np.array(lst)
    return list(-lst)


def invert(lst):
    return list(map(lambda x: -x, lst))

result = invert_np([1,-2,3,-4,5])
print(result)
