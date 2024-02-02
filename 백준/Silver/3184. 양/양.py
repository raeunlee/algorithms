# 백준 양
from collections import deque

r, c = map(int, input().split())
madang = []

for i in range(r):
    madang.append(list(input()))

dx = [1, -1 , 0, 0]
dy = [0, 0, 1, -1]
            
def bfs(x,y):
    global o_sum, v_sum
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    v_count = 0
    o_count = 0
    if madang[x][y] == 'v':
        v_count += 1
    elif madang[x][y] == 'o':
        o_count += 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if madang[nx][ny] == 'v':
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    v_count += 1
                elif madang[nx][ny] == 'o':
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    o_count += 1
                elif madang[nx][ny] == '.':
                    q.append((nx, ny))
                    visited[nx][ny] = True
 
    # 해당 구간에서 양이 더 많으면?
    if o_count > v_count:
        o_sum += o_count
    else: # 늑대가 더 많다면?
        v_sum += v_count
    
   
     
visited = [[False] * c for _ in range(r)]
v_sum = 0
o_sum = 0

for i in range(r):
    for j in range(c):
        if not visited[i][j]:
            if madang[i][j] == '.' or madang[i][j] == 'v' or madang[i][j] == 'o':
                bfs(i,j)

print(o_sum, v_sum)
            
                
