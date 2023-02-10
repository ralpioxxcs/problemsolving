n, k = map(int, (input().split()))
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)
for idx in range(k):
    if a[idx] < b[idx]:
        a[idx] = b[idx]
print(sum(a))