#미로탐색
from collections import deque
import sys
input = sys.stdin.readline


dx = [0,1,0,-1]
dy = [1,0,-1,0]
n, m = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]* M for _ in range(M)]



for i in range(n):
    numbers = list(input)
    for j in range(m):
        A[i][j] = int(numbers[j])

def BFS(i, j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True

    while queue:
        now = queue.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]