def solve(k,n): # k층수, n호수
    if k == 0:
        return n
    sum = 0
    for v in range(1, n+1):
        sum += solve(k-1,v)
    return sum

T = int(input())
for v in range(T):
    k = int(input())
    n = int(input())
    print(solve(k,n))
