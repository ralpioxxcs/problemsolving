h = 10
bowls = list(str(input()))
for i in range(1,len(bowls)):
  if bowls[i] == bowls[i-1]:
    h+=5
  else:
    h+=10
print(h)