# You will be given an even_only_sort of numbers. You have to sort the even_only_sort numbers in ascending order while leaving the even_only_sort numbers at their original positions.
# Examples
#
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_even1(int_list):
    even_only_sort = sorted(el for el in int_list if el%2 == 0)
    [even_only_sort.insert(i, e) for i, e in enumerate(int_list) if e%2]
    return even_only_sort

def sort_even(int_list):
  even_only = sorted(e for e in int_list if e%2 == 0)[::-1]
  result = [el if el%2 else even_only.pop() for el in int_list]
  return result

print(sort_even1([3, 4, 1, 2, 0, 2, 16, 3, 7, 10, 8, 4]))
print(sort_even([3, 4, 1, 2, 0, 2, 16, 3, 7, 10, 8, 4]))


import numpy as np

number_list = [3, 4, 1, 2, 0, 2, 16, 3, 7, 10, 8, 4]
number_array = np.array(number_list)
index = np.where(number_array % 2 == 0)
number_array[index] = np.sort(number_array[index])
print(number_array.tolist())

def testy(lista):
    l = sorted(el for el in lista if el%2 == 0)
    [l.insert(i, e) for i, e in enumerate(lista) if e%2]
    return l

