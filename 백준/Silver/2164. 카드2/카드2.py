from collections import deque

n = int(input())
q = deque()

for i in range(1, n+1):
    q.append(i)

while len(q)>1:
    q.popleft() #맨위 제거
    tmp = q.popleft()
    q.append(tmp)
    
print(q.popleft())

    