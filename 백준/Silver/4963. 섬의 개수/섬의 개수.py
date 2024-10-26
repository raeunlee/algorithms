# 50 * 50 * 50 * 4 = 5000000

from collections import deque

# 위 아래 양 옆 대각선 8방향
dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,1,-1,1,-1]

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        exit(0)
        
    else:
        graph = []
        q = deque()
        
        for i in range(h):
            row = list(map(int, input().split()))
            graph.append(row)
            
        visited = [[False] * w for _ in range(h)]
        
        count = 0 
        
        for j in range(h):
            for i in range(w):
                if graph[j][i] == 1 and not visited[j][i]:
                    q.append((j,i))
                    visited[j][i] = True
                    while q:
                        y, x = q.popleft()
                        for i in range(8):
                            nx = x + dx[i]
                            ny = y + dy[i]
                            if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and graph[ny][nx] == 1:
                                q.append((ny, nx))
                                visited[ny][nx] = True
                    count += 1
                    
        print(count)
                    
                        
                    
                
        
        