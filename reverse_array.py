def digitize(n):

    return list(map(int, str(n)[::-1]))

wynik = digitize(123456789)
print(type(wynik[0]))