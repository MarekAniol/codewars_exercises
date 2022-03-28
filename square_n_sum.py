# Complete the square sum function so that it squares each number passed into it and then sums the results together.
#
# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

def square_sum(numbers: list) -> int:
    return sum([i**2 for i in numbers])

wynik = square_sum([1, 2, 2])
print(wynik)