from collections import deque

def solution(people, limit):
    count = 0		# 보트 갯수
    people.sort()
    q = deque(people)
    
    # 보트엔 최대 2명
    while len(q) > 1:
        # 무게 합이 맞는 경우 양쪽에서 제거
        if q[0] + q[-1] <= limit:
            q.pop()
            q.popleft()
            count += 1
            continue
        # 무게 합 넘는경우, 큰 무게만 제거
        else:
          count += 1
          q.pop()
    
    # 사람 남아있으면 +1
    if q:
        count += 1
    
    return count

#def solution(people, limit):
    #count = 0		# 보트 갯수
    #weightSum = 0	# 무게 합
    #for index in range(len(people)):
    #    weightSum += people[index]
    #    
    #    # case1) 현재까지 무게합이 제한에 딱 맞는경우 보트갯수 +1
    #    if weightSum == limit:
    #        weightSum = 0
    #        count += 1
    #    # case2) 무게합이 제한을 넘는경우, 보트갯수 +1, 현재 무게 유지
    #    elif weightSum > limit:
    #        weigthSum = people[index]
    #        count += 1
    #    
    #    # 마지막 사람인경우, 보트 +1
    #    if index == len(people)-1 and weightSum != 0:
    #        count += 1
    #        continue
        