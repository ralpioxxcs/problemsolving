t = int(input())
for _ in range(t):
  s = list(str(input()))
  score = 0
  increment = 1
  for i in range(0,len(s)):
    if s[i] == 'O':
      score+=increment
    elif s[i] == 'X':
      increment=1
    if i != len(s)-1 and s[i] == s[i+1] == 'O':
      increment+=1
  print(score)
