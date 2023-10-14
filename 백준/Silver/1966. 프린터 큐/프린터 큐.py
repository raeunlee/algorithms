from collections import deque

n = int(input())
for i in range(n):
    N,M = map(int, input().split())
    L = deque(list(map(int, input().split())))
    idx = deque(list(range(N)))
    cnt = 0
    
    while L:
        if L[0] == max(L):
            cnt += 1
            L.popleft()
            
            pop_idx = idx.popleft()
            if pop_idx == M:
                print(cnt)
        else:
            L.append(L.popleft())
            idx.append(idx.popleft())