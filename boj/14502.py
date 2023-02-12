from collections import deque
import copy

moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]

# 전염
def infect():
  land_infested = copy.deepcopy(land)

  q = deque()
  for virus in viruses:
    q.append(virus)

  while (q):
    virus = q.popleft()

    for move in moves:
      cx = virus[0] + move[0]
      cy = virus[1] + move[1]
      if cx < 0 or cx >= n or cy < 0 or cy >=m:
        continue
      if land_infested[cx][cy] == 0:
        land_infested[cx][cy] = 2
        q.append((cx,cy))

  global empty_count
  cur_empty_count = 0
  for i in range(n):
    cur_empty_count += land_infested[i].count(0)

  empty_count = max(empty_count, cur_empty_count)

def set_wall():
  for i in range(len(emptys)):
    for j in range(0, i):
      for k in range(0, j):
        wall_1 = emptys[i]
        wall_2 = emptys[j]
        wall_3 = emptys[k]

        land[wall_1[0]][wall_1[1]] = 1
        land[wall_2[0]][wall_2[1]] = 1
        land[wall_3[0]][wall_3[1]] = 1
        infect()
        land[wall_1[0]][wall_1[1]] = 0
        land[wall_2[0]][wall_2[1]] = 0
        land[wall_3[0]][wall_3[1]] = 0

# 벽 만들기 (dfs)
def set_wall_dfs(wall_count):
  # 벽을 3개 세웠을경우 중지
  if wall_count == 3:
    infect()
    return

  for i in range(n):
    for j in range(m):
      if land[i][j] == 0:
        land[i][j] = 1
        set_wall(wall_count + 1)
        land[i][j] = 0

  return

#==============================================================================
n,m = map(int, input().split())

viruses = []
emptys = []
land = []

for i in range(n):
  spaces = list(map(int,input().split()))
  for j in range(len(spaces)):
    if spaces[j] == 2: # 바이러스 위치 저장
      viruses.append((i,j))
    elif spaces[j] == 0:
      emptys.append((i,j))
  land.append(spaces)

wall_count = 0
empty_count = 0
set_wall()
print(empty_count)