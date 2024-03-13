# A -> B
from collections import deque

a, b = map(int, input().split())
q = deque()
q.append([a,0]) # 현재 숫자와 연산 횟수
visited = set()
ans = -1
while q:
    now, cnt = q.popleft()
    
    if now == b:
        ans = cnt
        break
        
    mul = now * 2
    if mul not in visited and mul <= b * 2 :
        q.append([mul, cnt+1])
        visited.add(mul)

    add =  now * 10 + 1
    if add not in visited and add <= b * 2:
        q.append([add, cnt + 1])
        visited.add(add)

if ans >= 0:
    print(ans + 1)
else:   
    print(ans)