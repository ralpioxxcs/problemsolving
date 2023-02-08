n = int(input())    # 집 갯수
costs = []          # R,G,B 칠하는 비용 (0 <= n <= 1000)
for _ in range(n):
    costs.append(list(map(int,input().split())))

cache = [[0]*3 for x in range(n)]

# 초기값
cache[0][0] = costs[0][0]
cache[0][1] = costs[0][1]
cache[0][2] = costs[0][2]

# 집 갯수만큼 순회하며 계산 (다음 집(1) 부터 시작)
for index in range(1,n):
    # R
    cache[index][0] = min(costs[index][0] + cache[index-1][1], costs[index][0] + cache[index-1][2])
    
    # G
    cache[index][1] = min(costs[index][1] + cache[index-1][0], costs[index][1] + cache[index-1][2])
    
    # B
    cache[index][2] = min(costs[index][2] + cache[index-1][0], costs[index][2] + cache[index-1][1])
    
# 합산된 값의 최소값
print(min(cache[-1][0], cache[-1][1], cache[-1][2]))