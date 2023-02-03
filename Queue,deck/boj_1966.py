import sys
from collections import deque
L = deque()
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    N,M = map(int, sys.stdin.readline().split())
    L.append(sys.stdin.readline().split())
    print(*L)
    
    for j in range(N):
        if L[j] < L[j+1]:
            L.append(L.popleft())
            print(L)
        elif L[j] == L[M]:
            L.append(L.popleft())
            print(L)
        else:
            break