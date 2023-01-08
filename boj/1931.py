import sys 
conference = []
for _ in range(int(sys.stdin.readline())):
  conference.append(list(map(int, sys.stdin.readline().split())))

conference = sorted(sorted(conference, key=lambda c:c[0]), key=lambda c:c[1])

count = 1
end = conference[0][1]
for i in range(1,len(conference)):
  if conference[i][0] >= end:
    count+=1
    end = conference[i][1]
print(count)