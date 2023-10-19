from collections import deque

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)] # 가로 n 만큼의 세로 m 을 0 으로 채워주기
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split()) #꼭지점입력받기
    for i in range(x1,x2): #가로길이만큼
       for j in range(m-y1-1, m-y2-1, -1):
           graph[j][i] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 1 # 방문처리 해준다
    size = 1 #체크할 너비
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n and graph[nx][ny]==0:
                size += 1
                graph[nx][ny] = 1
                q.append((nx,ny))
    ans.append(size)
    
ans = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            bfs(i,j)
ans.sort()
print(len(ans))
for i in ans:
    print(i, end=' ')
