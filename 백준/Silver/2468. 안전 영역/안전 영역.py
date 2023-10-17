from collections import deque

n = int(input())
graph = []
maxNum = 0
 
for i in range(n): #한 줄 씩 입력받기
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > maxNum: #가장높은곳을 찾는것임
            maxNum = graph[i][j] 

# 상하좌우 이동
dx = [0 ,0, 1, -1]
dy = [1, -1, 0 ,0]   
       
def bfs(x, y, num, visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1 
    while q:
        x, y = q.popleft()
        for i in range(4): #4방향으로 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > num and visited[nx][ny] == 0:
                    visited[nx][ny] = 1 #방문처리
                    q.append((nx, ny))
    
result = 0

for i in range(maxNum):
    visited = [[0] * n for i in range(n)]
    cnt = 0
    
    #이중 배열 돌기
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i, visited)
                cnt+=1
    
    if result < cnt:
        result = cnt
        
print(result)