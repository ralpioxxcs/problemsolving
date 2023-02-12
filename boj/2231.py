n = int(input())

ans = n
c = n
# c을 감소시키면서 검사
while (c):
    nums = [int(x) for x in str(c)]

    cur = int(c)
    for num in nums:
        cur += num

    if cur == n:
        ans = min(cur, c)

    c -= 1

if ans == n:
   print(0)
else:
   print(ans)
