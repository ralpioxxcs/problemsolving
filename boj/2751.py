import sys
nums = []
for _ in range(int(input())):
    nums.append(int(sys.stdin.readline()))
nums.sort()
for v in nums:
    print(v)