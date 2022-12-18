N,M = map(int, input().split())
nums = []

def solve():
    if len(nums) == M:
        print(' '.join(map(str,nums)))
        return

    for v in range(1,N+1):
        if nums.count(v) > 0:
            continue
        nums.append(v)
        solve()
        nums.pop()

solve()
