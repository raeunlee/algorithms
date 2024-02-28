#섬의 개수
import sys
from collections import deque
input = sys.stdin.readline

# 위 아래 양 옆 대각선 4방향
dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,1,-1,1,-1]

def bfs(x,y):
    visited[x][y] = True
    
    q = deque()
    q.append([x,y])
    
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<h and 0<=ny<w:
                if visited[nx][ny]== False and land[nx][ny]==1:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    
    
    
    


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    land = []
    visited = [ [False] * w for _ in range(h)]
    answer = 0
    for i in range(h):
        land.append(list(map(int, input().split())))
    for x in range(h):
        for y in range(w):
            if land[x][y] == 1 and visited[x][y] == False:
                bfs(x,y)
                answer += 1
                
    print(answer)