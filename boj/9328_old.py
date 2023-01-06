import sys

# input
h = 0
w = 0
floor = []
visited = []
keys = []

# runtime
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
paths = []  # discovered
doors = {}
docs = 0  # found documents

def solve(startX, startY: int):
  global docs

  if floor[startX][startY] == '*':
    return
  elif floor[startX][startY] == '$':
    docs += 1
    floor[startX][startY] = '.'
  elif floor[startX][startY].isupper():
    if floor[startX][startY].lower() in keys:
      floor[startX][startY] = '.'
    else:
      doors[floor[startX][startY]] = {'x': startX, 'y': startY}
      return
  elif floor[startX][startY].islower():
    if floor[startX][startY].upper() in doors:
      paths.append({'x': doors[floor[startX][startY].upper()]['x'], 
                    'y': doors[floor[startX][startY].upper()]['y']})
    keys.add(floor[startX][startY].lower())
    floor[x][y] = '.'
    visited[x][y] = 0

  # discover up,left,right,down
  paths.append({'x': startX, 'y': startY})
  while len(paths):
    cur = paths.pop()

    if visited[cur['x']][cur['y']]:
      continue
    else:
      visited[cur['x']][cur['y']] = 1

    for idx in range(4):
      x = cur['x'] + dx[idx]
      y = cur['y'] + dy[idx]
      if x < 0 or x >= h or y < 0 or y >= w:
        continue
      what = floor[x][y]
      if what == '.':
        paths.append({'x': x, 'y': y})
      elif what == '*':
        continue
      elif what == '$':
        docs += 1
        floor[x][y] = '.'
        paths.append({'x': x, 'y': y})
      elif what.isupper():
        if what.lower() in keys:
          floor[x][y] = '.'
          visited[x][y] = 0
          paths.append({'x': x, 'y': y})
        else:
          doors[what] = {'x': x, 'y': y}
          continue
      elif what.islower():
        if what.upper() in doors:
          # 저장해 두었던 door의 좌표 입력
          paths.append({'x': doors[what.upper()]['x'], 
                        'y': doors[what.upper()]['y']})
        keys.add(what.lower())
        floor[x][y] = '.'
        visited[x][y] = 0
        paths.append({'x': x, 'y': y})

for _ in range(int(input())):
  h, w = map(int, input().split())
  floor = [list(input()) for _ in range(h)]
  keys = set(input())

  visited = [[0 for _ in row] for row in floor]
  docs = 0
  for i in range(h):
    for j in range(w):
      if (i == 0 or i == h - 1 or j == 0 or j == w - 1):
        solve(i, j)
  print(docs)