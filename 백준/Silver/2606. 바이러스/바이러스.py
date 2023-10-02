from collections import deque

n = int(input())
m = int(input())

coms = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    coms[a].append(b)
    coms[b].append(a)

def bfs(coms, c):
    global cnt
    q = deque([c]) 
    while q:
        pop = q.popleft()
        visited[pop] = True
        for i in coms[pop]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)
                cnt += 1
    print(cnt)

bfs(coms, 1)               
                
    
        
