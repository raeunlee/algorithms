from collections import deque

n = int(input())

l = []

for _ in range(n+1):
    l.append([])

for i in range(n-1):
    a, b = map(int, input().split())
    l[a].append(b)
    l[b].append(a)
    
def bfs(now):
    q.append(now)
    visited[now] = True
    parent[now] = 0 # 일단 없다
    while q: 
        now = q.popleft()
        for node in l[now]: # 현재 노드에 연결된 노드들 확인
            if not visited[node]: # 방문하지 않은 노드
                q.append(node)
                visited[node] = True # 방문
                parent[node] = now # 방문하는 노드의 부모는 현재 나
    
q = deque()

visited = [False] * (n+1)
parent = [0] * (n+1)

# 트리 방문 순서는 부모 -> 자식, 루트노드에서 시작
bfs(1)

for i in range(2, n+1):
    print(parent[i])