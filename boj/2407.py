n,m=map(int,input().split())
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
print(fact(n)//(fact(n-m)*fact(m)))