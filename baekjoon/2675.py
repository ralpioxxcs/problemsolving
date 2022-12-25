t = int(input())
for _ in range(t):
  r,s = input().split()
  concat = []
  for v in (list(str(s))):
    for _ in range(int(r)):
      concat+=v
  print(''.join(map(str,concat)))