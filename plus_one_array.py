# Given an lstay of integers of any length, return an lstay that has 1 added to the value represented by the lstay.
#
#     the lstay can't be empty
#     only non-negative, single digit integers are allowed
#
# Return nil (or your language's equivalent) for invalid inputs.
# Examples
#
# For example the lstay [2, 3, 9] equals 239, adding one would return the lstay [2, 4, 0].
#
# [4, 3, 2, 5] would return [4, 3, 2, 6]
def up_lst(lst):
    return None if (any(filter(lambda x: x < 0 or len(str(x)) > 1, lst)) or not lst) else [int(el) for el in list(str(int("".join(map(str, lst))) + 1))]


print(up_lst([]))

