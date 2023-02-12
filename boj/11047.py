n, k = map(int, input().split())
values = [int(input()) for x in range(n)]
values.sort(reverse=True)
coin = 0
while(k):
    for v in values:
        if k < v: continue
        coin += k // v
        k %= v
print(coin)