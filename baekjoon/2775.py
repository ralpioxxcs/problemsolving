T = int(input())
for v in range(T):
    sum = [x+1 for x in range(14)] # 0층 인원 초기화
    k = int(input())    # 층
    n = int(input())    # 호
    for kk in range(k):
        for nn in range(1, n):
            sum[nn] += sum[nn-1]
    print(sum[n-1])