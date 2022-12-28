c = 100
y = 100
for _ in range(int(input())):
  c_,y_ = map(int,input().split())
  if c_ > y_:
    y -= c_
  elif c_ < y_:
    c -= y_
print("{}\n{}".format(c,y))