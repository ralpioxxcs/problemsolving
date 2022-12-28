n = int(input())
if n == 1: exit
pfs = []
while True:
  if n == 1:
    break;
  i = 2
  while True:
    if n % i == 0 :
      n  = n//i
      pfs.append(i)
      break
    else:
      i+=1
[print(x) for x in pfs]