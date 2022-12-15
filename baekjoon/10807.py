import sys

N = int(input())
data = list(map(int,sys.stdin.readline().split()))
target = int(input())
count = 0
for v in data:
    if target == v:
        count+=1
print(count)
