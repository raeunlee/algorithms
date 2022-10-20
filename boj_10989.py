# 수 정렬하기3
## counting 정렬 카운팅정렬, 계수 정렬사용할것


import sys
n = int(sys.stdin.readline())

b = [0] * 10001

for i in range(n):
    b[int(sys.stdin.readline())] += 1
    
for i in range(10001):
    if b[i] != 0:
        for j in range(b[i]):
            print(i)