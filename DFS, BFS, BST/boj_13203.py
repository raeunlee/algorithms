#친구관계 ABCDE, 깊이가 4인지 아닌지임 

import sys
input = sys.stdin.readline

finshed = False #그래프가 끝이 나는지 안나는지 구분 
n, m = map(int, input().split()) #친구 5, 관계 4
graph = [[] for _ in range(n)] # N개 만큼의 빈 그래프 생성 
visited = [False] * n 

#그래프 채우기
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1) 

# print(graph)

#시작점, 깊이
def dfs(start, depth):
    global finshed #전역변수 선언 
    visited[start] = True

    if depth == 4: #깊이가 4이면 끝까지 감 
        finshed = True
        return
    for i in graph[start]:
        if not visited[i]:
            dfs(i, depth + 1) 
            visited[i] = False

for i in range(n):
    dfs(i, 0)
    visited[i] = False
    if finshed:
        break

print(1 if finshed else 0)