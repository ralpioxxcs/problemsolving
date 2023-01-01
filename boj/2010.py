import sys
count = 0
for _ in range(int(sys.stdin.readline().rstrip())-1):
  n = int(sys.stdin.readline().rstrip())
  count += n-1
print(count+int(sys.stdin.readline().rstrip()))