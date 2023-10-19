
from collections import deque

n = int(input())
color = []
visited = [[False] * n for _ in range(n)]

for i in range(n): #한 줄 씩 입력받기
    color.append(list(input().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs1(x,y):
    visited[x][y] = True #방문처리 해줌
    q = deque()
    q.append((x,y))
   # now_color = color[x][y] #지금 내 색깔
    while q: 
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if color[nx][ny] == color[x][y] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                               

count1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs1(i,j)
            count1 += 1
print(count1, end=' ')

#색약 0 
count2 = 0
visited = [[False] * n for _ in range(n)]
#R을 G로 바꿔주기            
for i in range(n):
    for j in range(n):
        if color[i][j]=='R':
            color[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs1(i,j)
            count2 += 1
print(count2)





    







