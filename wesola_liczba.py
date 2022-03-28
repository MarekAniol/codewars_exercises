def funy_number(x: int) -> int:
    print(len(str(x)))
    y = [int(el) for el in list(str(x))]
    x = sum(y)
    print(x)
    return funy_number(x) if x >= 10 else 1
