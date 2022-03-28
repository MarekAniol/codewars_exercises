def fib():
  a = 0
  b = 1
  while b < 200:
    yield a
    a, b = b, a + b

def fib2(a=0, b=1):
  fib = [a, b]
  while b < 100:
    fib.append(a + b)
    a, b = b, a + b
  return fib











