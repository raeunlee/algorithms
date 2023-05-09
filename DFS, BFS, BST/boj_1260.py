#dfs-stack, bfs-queue
import sys
from collections import deque

input = sys.stdin.readline

def dfs(x):
    print(x, end=' ')
    visited[x] = 1
    for i in adj[x]:
        if not visited[i] = 1
        dfs(i)
        
def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1
    print(x, end=' ')
    while q:
        x = q.popleft()
        