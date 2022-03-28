# Given an array of integers your solution should find the smallest integer.
#
# For example:
#
#     Given [34, 15, 88, 2] your solution will return 2
#     Given [34, -345, -1, 100] your solution will return -345
#
# You can assume, for the purpose of this kata, that the supplied array will not be empty.
def minimum_arr(arr):
    min_arr = min(arr)
    return min_arr

print(minimum_arr([2, -5, 120]))