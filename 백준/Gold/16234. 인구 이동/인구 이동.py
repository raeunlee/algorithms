# 인구이동
from collections import deque
import sys
input = sys.stdin.readline

# 인구이동을 위해 인접한 나라를 탐색
def bfs(x,y,l,r):
    q = deque()
    q.append([x,y])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited[x][y] = True
    union = [[x,y]] # 연합에 속한 나라 좌표
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                # 인접한 나라와의 인구 수 차이가 l이상 r이하여야 함
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    visited[nx][ny] = True
                    q.append([nx,ny])
                    union.append([nx,ny]) # 연합에 추가
    
    if len(union) > 1:
        # union안의 좌표를 바탕으로 인구수 모두 더해주기
        avg_pop = sum([graph[cx][cy] for cx,cy in union]) // len(union)
        for cx, cy in union: # 연합안의 모든 좌표를 평균 인구수로 바꿔준다
            graph[cx][cy] = avg_pop
        return union # 연합 반환
    else:
        return []
# 메인
n, l, r = map(int, input().split())
graph = []
visited = [[False] * n for _ in range(n)] # 방문체크 배열
team = 0 # 연합의 개수
tmp_sum = 0 # 인구수
day = 0 # 날짜

# 연합 배열
for i in range(n):
    graph.append(list(map(int, input().split())))

# 탐색 시작
while True: 
    visited = [[False] * n for _ in range(n)] # 방문체크 배열
    moved = False
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union = bfs(i,j,l,r)
                if union : # 연합이 있다면?
                    moved = True
                    
    
    if not moved:
        break
    
    day += 1

print(day)