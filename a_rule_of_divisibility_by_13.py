def thirt(num):
    new_number = 0
    for n in range(len(str(num))):
        digit = num // 10 ** n % 10
        mod = ((10**n) % 13) * digit
        new_number += mod
    return thirt(new_number) if len(str(new_number)) > 2 else new_number


print(thirt(1000))
