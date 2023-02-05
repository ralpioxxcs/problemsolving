from enum import Enum

# move helper
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

class Space(Enum):
  EMPTY_SPACE = 1
  WALL = 2
  DOCUMENT = 3
  DOOR = 4
  KEY = 5

def checkRange(x: int, y: int):
  if x < 0 or x >= width or y < 0 or y >= height:
    return False
  return True

def checkSpace(what):
  if what == '.':
    return Space.EMPTY_SPACE
  elif what == '*':
    return Space.WALL
  elif what == '$':
    return Space.DOCUMENT
  elif 'A' <= what <= 'Z':
    return Space.DOOR
  elif 'a' <= what <= 'z':
    return Space.KEY

def solve(y: int, x: int):
  global documents
  global doors
  paths = []  # discovering paths (queue)

  what = floor[y][x]
  space = checkSpace(what)

  if space == Space.WALL:
    return
  elif space == Space.DOCUMENT:
    documents += 1
    floor[y][x] = '.'
  elif space == Space.DOOR:
    if what.lower() in keys:
      floor[y][x] = '.'
    else:
      doors[what].add((x,y))
      return
  elif space == Space.KEY:
    if what.upper() in doors:
      for x,y in doors[what.upper()]:
        paths.append({'x': x, 'y': y})
    keys.add(floor[y][x].lower())
    floor[y][x] = '.'

  paths.append({'x': x, 'y': y})

  while (len(paths)):
    cur = paths.pop()

    # 중복 탐색 방지
    if visited[cur['y']][cur['x']]:
      continue
    else:
      visited[cur['y']][cur['x']] = 1

    for idx in range(4):
      curX = cur['x'] + dx[idx]
      curY = cur['y'] + dy[idx]
      if not checkRange(curX, curY):
        continue

      # 현재 자리 체크
      what = floor[curY][curX]
      space = checkSpace(what)
      if space == Space.WALL:
        continue
      elif space == Space.DOCUMENT:
        documents += 1
        floor[curY][curX] = '.'
        paths.append({'x': curX, 'y': curY})
      elif space == Space.DOOR:
        # 현재 갖고있는 키중에 해당하는 키가 있는지 체크
        if what.lower() in keys:
          floor[curY][curX] = '.'
          visited[curY][curX] = 0
          paths.append({'x': curX, 'y': curY})
        # 키를 갖고있지 않으면 열리지 않은 문 리스트에 추가
        else:
          doors[what].add((curX,curY))
      elif space == Space.KEY:
        if what.upper() in doors:
          for x,y in doors[what.upper()]:
            paths.append({'x': x, 'y': y})
        keys.add(what)
        floor[curY][curX] = '.'
        visited[curY][curX] = 0
        paths.append({'x': curX, 'y': curY})
      elif space == Space.EMPTY_SPACE:
        paths.append({'x': curX, 'y': curY})

for _ in range(int(input())):
  height, width = map(int, input().split())
  floor = [list(input()) for _ in range(height)]
  keys = set(input())
  visited = [[0 for _ in row] for row in floor]
  documents = 0

  doors = {}  # 열리지 않은 문 리스트
  for door in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    doors.setdefault(door, set()) 

  print(doors)
  if 'A' in doors:
    print('hi')

  doors['A'].add((2,3))
  for x,y in doors['A']:
    print('t',x,y)

  for i in range(height):
    for j in range(width):
      # visit only edge of the map
      if (i == 0 or i == height - 1 or j == 0 or j == width - 1):
        solve(i, j)

  print(documents)