# # input
# checkers = []
# for _ in range(int(input())):
#   checkers.append(tuple(map(int,input().split())))

# checkers = sorted(checkers, key=lambda c:abs(c[0]-c[1]))
# print(checkers)

# calcMove = lambda v1,v2:abs(v1[0] - v2[0]) + abs(v1[1] - v2[1])

# # solve
# answers = []
# for v in range(0, len(checkers)):
#   ans = []
#   k = v+1
#   print("goal: ",k)

#   # 모일 좌표를 변경해가면서 확인 [O(n)]
#   for center in checkers:
#     print("center: ", center)

#     for j in range(len(checkers)):
#       movements = []
#       print("current checker: ", checkers[j])

#       # 최소 k개의 체커를 모을때까지
#       while len(movements) != k: 
#         movements.append(calcMove(checkers[j],center))

#     ans.append(movements)

#   answers.append(min(ans))

# print(''.join(answers))