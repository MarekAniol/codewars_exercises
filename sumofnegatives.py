# Given an array of integers.
#
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative
# numbers. 0 is neither positive nor negative.
#
# If the input is an empty array or is null, return an empty array.
# Example
#
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
import math
def count_positives_sum_negatives(arr):
    positives = [pos for pos in arr if pos > 0]
    negatives = [neg for neg in arr if neg < 0]
    return [] if not arr else [len(positives), sum(negatives)]




result = count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])
print(result)
