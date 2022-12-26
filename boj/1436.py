N = int(input())
ans = [666]
num = 666

def isRight(n):
  numStr = list(map(str, str(num)))
  sixCount = 0
  sixFlag = False

  for v in numStr:
    if sixFlag == True:
      if v != '6':
        sixFlag = False
        sixCount = 0
      elif v == '6':
        sixCount += 1
        if sixCount >= 3:
          return True
    else:
      if v == '6':
        sixFlag = True
        sixCount += 1

  return False

while True:
  if len(ans) == N:
    break
  num += 1
  if isRight(num):
    ans.append(num)

print(ans[N-1])