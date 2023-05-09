# 연결요소의 개수
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split()) #
A = [[] for _ in range(n+1)] #인접리스트 초기화, 노드 n개이므로 n만큼 만들어주기
visited = [False] * (n+1) #방문리스트 초기화



for i in range(m):
    u, v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)

def DFS(x):
    visited[x] = True
    if not visited:
        DFS(x) #재귀



count = 0

for j in range(n+1):
    if not visited(j):
        count +=1
        DFS(j)
print(count)
        
    