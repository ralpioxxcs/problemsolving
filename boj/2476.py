n = int(input())
scores = []
for _ in range(n):
  score = 0
  a,b,c = map(int,input().split())
  if a == b == c:
    score += 10000 + (a*1000)
  elif a == b or a == c:
    score += 1000 + (a*100)
  elif b == c:
    score += 1000 + (b*100)
  elif a != b != c:
    score += (max(a,b,c)*100)
  scores.append(score)
print(max(scores))