q1 = q2 = q3 = q4 = axis = 0
for _ in range(int(input())):
  a,b=map(int,input().split())
  if a > 0 and b > 0:
    q1+=1
  elif a < 0 and b > 0:
    q2+=1
  elif a > 0 and b < 0:
    q4+=1
  elif a < 0 and b < 0:
    q3+=1
  else:
    axis+=1
print("Q1: {}\nQ2: {}\nQ3: {}\nQ4: {}\nAXIS: {}".format(q1,q2,q3,q4,axis))