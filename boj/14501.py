n = int(input()); days = []; pays = []
maxRev = 0

def dfs(day,pay):
    global maxRev
    if day+1 + days[day] > n+1:
        maxRev = max(maxRev, pay-pays[day])
        return
    elif day+1 + days[day] == n+1:
        maxRev = max(maxRev, pay)
        return

    for v in range(day + days[day], n):
        dfs(v, pay + pays[v])

for _ in range(n):
    t_,p_ = map(int,input().split())
    days.append(t_)
    pays.append(p_)

for i in range(n):
    dfs(i, pays[i])

print(maxRev)