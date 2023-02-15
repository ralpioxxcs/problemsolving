import sys 
t = int(sys.stdin.readline())
for _ in range(t):
  scores = []
  for _ in range(int(sys.stdin.readline())):
    first, second = map(int, sys.stdin.readline().split())
    scores.append((first, second))
  
  scores.sort(key=lambda item: item[0])

  # 서류 1등은 무조건 뽑힘
  cnt = 1
  highest = scores[0]
  for i in range(len(scores)):
    # 내 면접순위보다 높으면 너넨 뽑힘
    if highest[1] > scores[i][1]:
      # 다음부터는 내 면접순위랑 비교해야 함
      highest = scores[i]
      cnt += 1

  print(cnt)