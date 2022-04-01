from string import ascii_lowercase
def grid(n):
    lc = list(ascii_lowercase)
    for _ in lc:
        line = " ".join(lc[0:n])
        lc.append(lc.pop(0))
        yield line
