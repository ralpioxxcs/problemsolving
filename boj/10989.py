# 계수 정렬 문제
import sys

# 주어지는 숫자는 0부터 10000까지이므로 10000 length의 리스트를 미리 할당
nums = [0]*10001

for _ in range(int(input())):
    nums[int(sys.stdin.readline())] += 1
for idx in range (len(nums)):
    for v in range(nums[idx]):
      print(idx)