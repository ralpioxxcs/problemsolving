n = 10000
nums = [False] * (n+1)

def d(n):
  for v in list(str(n)):
    n += int(v)
  return n

for v in range(1,n+1):
  res = d(v)
  if res <= n:
    nums[d(v)] = True

for v in range (1,len(nums)):
  if nums[v] == False:
    print(v)