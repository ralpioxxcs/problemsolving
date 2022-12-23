n = int(input())
x = list(map(int,(input().split())))
xs = sorted(set(x))

def search(target,low,high):
  midIdx = int((low+high)/2)
  if xs[midIdx] == target:
    return midIdx
  elif target < xs[midIdx]:
    return search(target,low, midIdx-1)
  else:
    return search(target,midIdx+1, high)

print(' '.join(map(str,[search(i,0,len(xs)) for i in x])))