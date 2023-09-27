from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    q=deque()
    q.append([0, 0])
    visited[0][0] = 1
    
    dx,dy = [-1,1,0,0], [0,0,-1,1]
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1:
                     if visited[ny][nx] == -1:
                            visited[ny][nx] = visited[y][x] + 1
                            q.append([ny, nx])
                        
    answer = visited[-1][-1]
    return answer
