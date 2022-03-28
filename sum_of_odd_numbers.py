# Given the triangle of consecutive odd numbers:
#
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
#
# Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)
#
# 1 -->  1
# 2 --> 3 + 5 = 8

# 1 > 1
# 3 > 2   +2
# 7 > 3   +4
# 13 > 4  +6
# 21 > 5

# if n jest większe o 1 to pierwszy element listy jest

def row_sum_odd_numbers(n):
    first_element = 1
    for i in range(n):
        first_element += i * 2

    n_row = [first_element + i for i in range(0, 2*n, 2)]
    return sum(n_row)

print(row_sum_odd_numbers(13))

