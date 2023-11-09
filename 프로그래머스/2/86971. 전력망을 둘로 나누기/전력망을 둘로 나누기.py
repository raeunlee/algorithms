from collections import deque

def bfs(start,visited,graph):
    queue = deque([start]) #시작점
    result = 1
    visited[start] = True #방문처리
    while queue:
        now = queue.popleft() #현재지점
        
        for i in graph[now]:
            if visited[i] == False: 
                result += 1
                queue.append(i)
                visited[i] = True
                
    return result
        

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    
    for v1,v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
            
    for start, not_visit in wires: #시작점, 방문안한점 
        visited = [False]*(n+1)
        visited[not_visit] = True 
        result = bfs(start,visited,graph) 
        if abs(result - (n-result)) < answer:
            answer = abs(result - (n-result))
        
    return answer