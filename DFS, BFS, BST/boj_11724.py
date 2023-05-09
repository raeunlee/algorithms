# 연결요소의 개수
import sys
sys.setrecursionlimit(10000)

n,m = map(int, sys.stdin.readline().split())
A = [[]for _ in range(n+1)] #노드 개수만큼 그래프 인접 데이터 리스트 생성하기
visited = [False] * (n+1) # 방문 기록 리스트는 False로 초기화 시킬 것

def DFS(v):
    visited[v] = True #리스트에 현재 노드 방문 기록
    for i in A[v]:
        if not visited[i]: #방문안하면 DFS실행하기, 재귀
            DFS(i) #재귀

for _ in range(m): #간선 개수만큼 탐색
    s,e = map(int, sys.stdin.readline().split())
    A[s].append(e) #양방향 에지, 양방향으로 더하기
    A[e].append(s)

count = 0

for i in range(1, n+1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)