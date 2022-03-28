# Some numbers have funny properties. For example:
#
#     89 --> 8¹ + 9² = 89 * 1
#
#     695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
#
#     46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
#
# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p
#
#     we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n.
#
# In other words:
#
#     Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
#
# If it is the case we will return k, if not return -1.
#
# Note: n and p will always be given as strictly positive integers.

def dig_pow(n, p):
    n_str = str(n)
    sum_n_digits_power = 0
    for i in range(0, len(n_str)):
        sum_n_digits_power += int(n_str[i])**(p+i)
    if sum_n_digits_power % n == 0:
        k = int(sum_n_digits_power/n)
        return k
    return -1

def dig_pow_2(n, p):
    sum = 0
    str_n = str(n)
    for i, j in enumerate(str_n):
        sum += pow(int(j), p+i)
    if sum % n == 0:
        k = sum // n
    return k if sum%n==0 else -1

print(dig_pow_2(46288, 3))


