def solve():
    global pairs
    global friends
    global visited
    
    next = -1
    ans = 0
    
    # 아직 짝이 되지 않은 친구로 시작
    for index in range(len(visited)):
        if visited[index] == False:
            next = index
            break
    
    # 0,1,2,3
    # 0,1 | 2,3
    # 0,2 | 1,3
    # 0,3 | 1,2
    
    # 종료 조건: 모든 쌍이 완성되었을때
    if (next == -1):
        return 1
    
    for index in range(next, len(visited)):
        # 아직 친구가 되지 않았고, 친구쌍에 있는 경우에만
        if visited[index] == False and [friends[next], friends[index]] in pairFriendsList or [friends[index], friends[next]] in pairFriendsList:
            visited[index] =  visited[next] = True
            ans += solve()
            visited[index] = visited[next] = False
        
    return ans
    

for _ in range(int(input())):
    n, m = map(int, input().split())
    pairFriends = list(map(int, input().split()))

    # TODO: list comprehension으로 바꿔보기
    pairFriendsList = []
    for i in range(0, len(pairFriends)//2):
        pairFriendsList.append([pairFriends[i*2], pairFriends[(i*2)+1]])

    # GOAL: 학생들을 중복없이 짝 지을 수 있는 경우의 수
    pairs = []
    friends = [_ for _ in range(n)]
    visited = [False for _ in range(n)]
    
    print(solve())