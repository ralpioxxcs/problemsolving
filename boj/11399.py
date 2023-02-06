n = int(input())
times = list(map(int, input().split()))
times.sort()
sum = 0
for t in range(len(times)):
    subSum = 0
    for k in range(t,-1,-1):
      subSum += times[k]
    sum += subSum
print(sum)