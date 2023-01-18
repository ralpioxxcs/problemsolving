covers = [
  [[0, 0], [1, 0], [0, 1]],  # ⌜
  [[0, 0], [0, 1], [1, 1]],  # ⌝
  [[0, 0], [1, 0], [1, 1]],  # ⌞
  [[0, 0], [1, 0], [1, -1]],  # ⌟
]

def checkNvisit(i: int, j: int, cover: list, depth: int, check: bool):
  if check == False:
    for elem in cover:
      nx = i + elem[0]
      ny = j + elem[1]
      visited[nx][ny] = -1
    return

  # check range
  for elem in cover:
    nx = i + elem[0]
    ny = j + elem[1]
    if nx < 0 or ny < 0 or nx >= h or ny >= w:
      return False
    if board[nx][ny] == '#':
      return False
    if visited[nx][ny] >= 0:
      return False

  # visit
  for elem in cover:
    nx = i + elem[0]
    ny = j + elem[1]
    visited[nx][ny] = 0

  return True


def solve(depth: int):
  cx = cy = -1
  found = False

  # cover를 놓을 수 있는 자리 탐색
  for j in range(h):
    for i in range(w):
      if board[j][i] == '.' and visited[j][i] < 0:
        cx = j
        cy = i
        found = True
        break
    if found:
      break

  # 모두 덮은 경우
  if cx == -1 and cy == -1 and depth == ableCount // 3:
    return 1

  coverSuccess = 0
  # 현재 자리를 기준으로 4종류의 cover를 놓을 수 있는지 체크
  for cover in covers:
    if checkNvisit(cx, cy, cover, depth, True):
      coverSuccess += solve(depth + 1)
      checkNvisit(cx, cy, cover, depth, False)

  return coverSuccess


for _ in range(int(input())):
  h, w = map(int, input().split())
  board = [list(input()) for _ in range(h)]
  visited = [[-1 for _ in range(w)] for _ in range(h)]

  ableCount = 0
  for j in range(h):
    for i in range(w):
      if board[j][i] == '.':
        ableCount += 1

  # 덮을 수 없는 경우
  if (ableCount) % 3 != 0:
    print('end', 0)
    exit(0)

  print(solve(0))
