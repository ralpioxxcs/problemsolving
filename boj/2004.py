n,m=map(int,input().split())

# combination : n!/(n-m)!*m!
def calcIndices(n,s):
  count = 0
  m = s
  while s<=n:
    count += n//s
    s*=m
  return count

print(calcIndices(10,2))

print(min(
  calcIndices(n,5) - calcIndices(n-m,5) - calcIndices(m,5), 
  calcIndices(n,2) - calcIndices(n-m,2) - calcIndices(m,2)
))