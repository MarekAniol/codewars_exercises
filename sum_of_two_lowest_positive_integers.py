def sum_two_smallest_numbers(numbers):
    sorted = numbers.sort()
    return sorted

def sum_two_smallest_numbers_2(numbers):
    sort = sorted(numbers)
    return sum(sort[:2])

print(sum_two_smallest_numbers_2([0, 34, 12, 18, 22]))