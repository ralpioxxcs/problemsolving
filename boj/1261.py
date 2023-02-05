from collections import deque

# move helper
mx = [0, 0, -1, 1]
my = [1, -1, 0, 0]

def check_range(x, y: int):
   return x < m and y < n and x >= 0 and y >= 0

def solve():
    global brks
    paths = deque()  
    paths.append((0, 0, 0)) # 초기위치, 벽 부순 횟수
    visited[0][0] = 1

    while (len(paths)):
      curPos = paths.popleft()
      cx = curPos[0]
      cy = curPos[1]
      brk = curPos[2]

      if cx == m - 1 and cy == n - 1:
         return brk

      for idx in range(4):
          nx = cx + mx[idx]
          ny = cy + my[idx]

          # 중복 방문 및 범위 예외 처리
          if check_range(nx, ny) == False:
             continue
          if visited[ny][nx] == 1:
             continue

          visited[ny][nx] = 1   # 방문 처리

          if maze[ny][nx] == 1:
            paths.append((nx, ny, brk + 1))    # 탐색 리스트 추가 (벽 카운팅 O)
          else:
            paths.appendleft((nx, ny, brk))    # 탐색 리스트 추가 (벽 카운팅 X)
            maze[ny][nx] = 0                   # 빈 공간 처리

    return 0

m, n = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]  # 0: empty, 1: wall
visited = [[0 for _ in r] for r in maze]
breaks = [[0 for _ in r] for r in maze]
print(solve())
