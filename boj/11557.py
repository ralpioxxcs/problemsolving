t = int(input())
def solve():
  n = int(input())
  maxv = 0
  univ = ""
  for _ in range(n):
    u,d= list(input().split())
    if int(d) > maxv:
      maxv = int(d)
      univ = u
  print(univ)
[solve() for _ in range(t)]