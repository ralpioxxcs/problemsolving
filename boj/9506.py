while True:
  n = int(input())
  if n == -1:
    break
  divs = [1]
  div = 2
  while divs[-1] < n:
    if n%(div) == 0:
      divs.append(div)
    div+=1
  if sum(divs[:-1]) == n:
    p = "{} =".format(n)
    for v in divs[:-1]:
      p += " {} +".format(v)
    print(p[:-1])
  else:
    print("{} is NOT perfect.".format(n))