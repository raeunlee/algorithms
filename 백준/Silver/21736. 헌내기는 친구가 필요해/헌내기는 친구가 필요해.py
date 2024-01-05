# 헌내기는 친구가 필요해 

from collections import deque
n, m = map(int, input().split())
map = []

for i in range(n):
    map.append(list(input()))

visited = [[False] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

#도연이의 위치
x = 0
y = 0

for i in range(n):   
    for j in range(m):
        if map[i][j] == 'I':
            x = i
            y = j

# O는 빈 공간, X는 벽, I는 도연이, P는 사람
# 항상 I에서 출발해서 O으로만 이동다니고, X론 못가고 P를 만나면 +1

# bfs
def bfs(a, b):
    global answer
    visited[a][b] = True
    q = deque()
    q.append((a,b))

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if map[nx][ny] == 'O' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif map[nx][ny] == 'P' and not visited[nx][ny]:
                    answer += 1
                    visited[nx][ny] = True
                    q.append((nx, ny)) 
                    

answer = 0
bfs(x, y)

if answer == 0:
    print('TT')
else:
    print(answer)