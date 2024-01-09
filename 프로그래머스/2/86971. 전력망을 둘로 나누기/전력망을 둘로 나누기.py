from collections import deque

def bfs(start, visited, graph ):
    q = deque([start])
    cnt = 1
    visited[start] = True
    while q:
        x = q.popleft() # 현재 지점
        for i in graph[x]: # graph[x] 안의 요소들
            if visited[i] == False: # 방문하지 않은 수라면 
                cnt += 1 # 카운드 세준다 
                q.append(i)
                visited[i] = True
    return cnt # cnt return 
        


def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]  
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    print(graph)
    
    for start, end in wires:
        visited = [False] * (n+1)
        visited[end] = True
        result = bfs(start, visited, graph)
        if abs(result - ( n - result)) < answer:
            answer = abs(result - (n - result))
            
    return answer