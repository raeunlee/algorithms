# 백준 전쟁 - 전투
from collections import deque
# 가로 세로
n, m = map(int, input().split())
war = []
for i in range(m):
    war.append(list(map(str, input().rstrip())))
    

def bfs_w(wy, wx):
    w = 0
    q.append((wy,wx))
    visited[wy][wx] = True
    while q:
        y, x = q.popleft()
        if war[y][x] == 'W':
            w += 1   
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and war[ny][nx] == 'W' and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny,nx))          
    w_l.append(w)

def bfs_b(by,bx):
    b = 0
    q.append((by,bx))
    visited[by][bx] = True
    while q:
        y, x = q.popleft()
        if war[y][x] == 'B':
            b += 1   
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and war[ny][nx] == 'B' and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny,nx))          
    b_l.append(b)    

w_l = []
b_l = []

q = deque()

dx = [1,-1,0,0]
dy = [0,0,1,-1]

visited= [[False] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if not visited[i][j] and war[i][j] == 'W':
            bfs_w(i,j)

visited = [[False] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if not visited[i][j] and war[i][j] == 'B':
            bfs_b(i,j) 
            
w_result = 0
for i in range(len(w_l)):
    w_result += w_l[i] * w_l[i] 

b_result = 0
for i in range(len(b_l)):
    b_result += b_l[i] * b_l[i] 

print(w_result, b_result)