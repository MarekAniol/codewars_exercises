# def reverse_seq(n):
#     return [-i for i in range(-n, 0)]


def reverse_seq(n):
    return list(range(1, n+1).__reversed__())


result = reverse_seq(5)
print(result)

