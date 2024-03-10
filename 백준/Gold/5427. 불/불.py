from collections import deque
t = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def out(a,b):
    q = deque()
    visited = [[0] * n for _ in range(m)]
    q.append((a,b))
    visited[a][b] = 1
    
    for i in range(m):
        for j in range(n):
            # 불이 있을 경우 방문처리 후 append
            if maps[i][j] == '*':
                visited[i][j] = -1
                q.append((i,j))
                
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x 
            ny = dy[i] + y
            # 4방향 탐색으로 밖으로 나갔을 때
            if nx < 0 or nx > m - 1  or ny < 0 or ny > n - 1 :
                if visited[x][y] > 0: # 사람이 이동할 경우 출발점에 저장된 값을 돌려줌
                    return visited[x][y]
            
            elif 0<=nx<m and 0<=ny<n: # 지도 안에 있고
                if maps[nx][ny] == '.': # 빈 공간일 때
                    if visited[x][y] > 0 and not visited[nx][ny]: #사람이 이동하면
                        visited[nx][ny] = visited[x][y] + 1 # 시간 + 1
                        q.append((nx,ny))
                    # 이동하는 것이 불이고, 도착지는 불이 아닐때
                    elif visited[nx][ny] >= 0 and visited[x][y] == -1:
                        visited[nx][ny] = -1 #도착지를 불로 바꿔줌
                        q.append((nx,ny))
    return 'IMPOSSIBLE'


for _ in range(t):
    n, m = map(int, input().split())
    maps = []
    for i in range(m):
        maps.append(list(map(str,input())))
    for i in range(m):
        for j in range(n):
            if maps[i][j] == '@':
                print(out(i,j))
                break