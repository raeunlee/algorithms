from collections import deque

n, m = map(int, input().split())

miro = [list(map(int, input())) for i in range(n)]
visited = [[False for i in range(m)] for i in range(n)]

q = deque()
q.append((0, 0)) #가장 첫번째 index 넣어준다

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

while q:
    y, x = q.popleft()
    visited[y][x] = True #방문처리를 해준다
    for i in range(4): #위아래좌우 탐색해준다
        ny = y + dy[i]
        nx = x + dx[i]
        #다음꺼가 1이고 nx, ny이 범위내에 있고, 방문하지 않았따면?
        if 0 <= ny < n and 0 <= nx < m:
            if miro[ny][nx] == 1 and visited[ny][nx] == False:
                q.append((ny, nx))
                miro[ny][nx] += miro[y][x]

print(miro[n-1][m-1])

