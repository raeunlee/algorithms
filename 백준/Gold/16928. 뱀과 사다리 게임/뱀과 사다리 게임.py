# 뱀과 사다리 게임
from collections import deque
# 10*10게임판
game = []
game = list(range(101))

dist = [-1] * 101 
dist[1] = 0

n, m = map(int, input().split())
for i in range(n):
    a, b = map(int, input().split())
    game[a] = b
for j in range(m):
    a, b = map(int, input().split())
    game[a] = b

q = deque()
q.append(1)

while q:
    x = q.popleft()
    for i in range(1,7):
        nx = x + i
        if nx > 100:
            continue
        nx = game[nx] # 사다리나 뱀이면 해당 칸으로 이동한다
        if dist[nx] == -1: # 방문하지 않은 곳이면?
            dist[nx] = dist[x] + 1 # 방문횟수를 +
            q.append(nx)
            
print(dist[100])
        