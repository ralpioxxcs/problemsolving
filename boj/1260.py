from collections import deque 

def DFS(vertex):
    dfs_result.append(vertex)

    for edge in graph[vertex]:
        if visited_dfs[edge] == True: 
           continue
        if len(graph[edge]) == 0:
           continue
        visited_dfs[edge] = True
        DFS(edge)

    return

def BFS(start):
    dq = deque()
    dq.append(start)

    while(len(dq)):
        vertex = dq.popleft()
        bfs_result.append(vertex)

        for edge in graph[vertex]:
            if visited_bfs[edge] == True: 
               continue
            if len(graph[edge]) == 0:
               continue
            visited_bfs[edge] = True
            dq.append(edge)

    return

#-------------------------------------------------------------------------------

# n: 정점의 갯수
# m: 간선의 갯수
# v: 시작 정점
n,m,v = map(int,input().split())

# 그래프 초기화
graph = {}
visited_dfs = {}
visited_bfs = {}
for index in range(1, n+1):
    graph.setdefault(index, [])
    visited_dfs.setdefault(index, False)
    visited_bfs.setdefault(index, False)

for _ in range(m):
    v1,v2 = map(int, input().split())
    # 양방향 간선 삽입
    graph[v1].append(v2)
    graph[v2].append(v1)

# 동일 간선 오름차순 정렬
for key in graph.keys():
    graph[key].sort()

dfs_result = []
bfs_result = []

# 첫번째 정점부터 시작
visited_dfs[v] = True
visited_bfs[v] = True
DFS(v)
BFS(v)

for v in dfs_result:
   print(v, end=" ")
print("")
for v in bfs_result:
   print(v, end=" ")