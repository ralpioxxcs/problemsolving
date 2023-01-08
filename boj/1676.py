n = int(input())
mem = {}
def fact(n):
  global mem
  if n == 0:
    return 1
  if n in mem:
    return mem[n]
  else:
    mem[n] = n * fact(n-1)
    return mem[n]
f = fact(n)
print(len(list(str(f))) - len(list(str(f).rstrip('0'))))