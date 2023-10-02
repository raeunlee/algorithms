
from collections import deque

n,m,k,x = map(int, input().split())

city = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    city[a].append(b)
    
distances = [-1] * (n+1) 
distances[x] = 0

q=deque([x])

while q:
    now = q.popleft()
    for next in city[now]:
        if distances[next] == -1 :
            distances[next] = distances[now] + 1
            q.append(next)

check = False

for i in range(1, n+1):
    if distances[i] == k:
        print(i)
        check = True

if check == False:
        print(-1)