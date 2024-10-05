from collections import deque

def solution(n, computers):
    
    graph = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(len(computers[i])):
            if computers[i][j] == 1 and i != j: # i, j 가 연결되어 있음
                graph[i].append(j)
    
    print(graph)
    
    # 전체 다 방문전으로 처리
    visited = [False] * n
    
    q = deque()

    def bfs(start):
        q.append(start)
        visited[start] = True
        while q:
            now = q.popleft()
            for nxt in graph[now]:
                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
        
    count = 0
    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            count += 1
   
    print(count)
    return count
            
        
