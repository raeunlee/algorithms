from collections import deque

def BFS(i):
    visited = [0] * (N+1)
    queue.append(i)
    visited[i] = 1
    while queue:
        t = queue.popleft()
        for v in graph[t]:
            if not visited[v]:
                visited[v] = visited[t]+1
                queue.append(v)
    return sum(visited)


N, M = map(int, input().split()) 
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
ans = []
for i in range(1, N+1):
    ans.append(BFS(i))

print(ans.index(min(ans))+1)