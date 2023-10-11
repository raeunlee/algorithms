import sys

# 찾고자 하는 숫자, 행, 열
n, r, c = map(int, sys.stdin.readline().split())

visit = 0

while n!= 0:
    n = n-1
    size = 2 ** n
    # 1사분면의 가로 < 2^(n-1), 세로 < 2^(n-1)

    if r < size and c < size :
        visit += 0
    
    # 2사분면의 가로 ≥ 2^(n-1), 세로 < 2^(n-1)
    elif r < size and c >= size :
        visit += size * size #2사분면의 시작점
        c -= size
        
    # 3사분면의 가로 < 2^(n-1), 세로 ≥ 2^(n-1)
    elif r>= size and c<size:
        visit += size * size * 2
        r -= size  
    
    # 4사분면의 가로 ≥ 2^(n-1), 세로 ≥ 2^(n-1)
    else:
        visit += size * size * 3
        r -= size
        c -= size

print(visit)