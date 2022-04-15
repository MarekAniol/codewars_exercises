from string import ascii_lowercase as lca


def grid_generator(n):
    lc = list((n // len(lca) + 1) * lca)
    for _ in range(n):
        line = " ".join(lc[0:n])
        lc.append(lc.pop(0))
        yield line


def grid(n):
    char = list((n // len(lca) + 1) * lca)
    row = 0
    r = ''
    while n > row:
        r += " ".join(char[0:n]) + "\n"
        char.append(char.pop(0))
        row += 1
    return None if n < 0 else r[0:-1]


for i in grid_generator(29):
    print(i)