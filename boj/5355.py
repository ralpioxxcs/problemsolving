t = int(input())
def check(operator, r):
  if operator == '@':
    return r*3
  elif operator == '%':
    return r+5
  elif operator == '#':
    return r-7
for _ in range(t):
  inputs = list(input().split())
  for v in inputs[1:]:
    inputs[0] = check(v,float(inputs[0]))
  print("{:0.2f}".format(inputs[0]))
