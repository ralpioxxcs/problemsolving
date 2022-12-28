ats = 300
bts = 60
cts = 10
T = int(input())
hist = []
a = b = c = 0
while True:
  if ats * a + bts * b + cts * c == T:
    print("{} {} {}".format(a,b,c))
    break
  elif ats * a + bts * b + cts * c > T:
    print(-1)
    break
  else:
    # greedy solution
    # highest time first (a>b>c)
    if ats * (a+1) + bts * b + cts * c <= T:
      a+=1
    elif ats * a + bts * (b+1) + cts * c <= T:
      b+=1
    elif ats * a + bts * b + cts * (c+1) <= T:
      c+=1
    else:
      print(-1)
      break