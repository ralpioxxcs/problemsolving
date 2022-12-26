s = int(input())
cnt = 0
inc = 0
while True:
  inc+=cnt
  if inc > s:
    print(cnt-1)
    break
  cnt+=1