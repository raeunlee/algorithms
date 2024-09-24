from collections import deque

r, c, n = map(int,input().split())

l = []

for _ in range(r):
    row = list(input())
    l.append(row)


n = n - 1 # 1초 동안은 아무것도 안함

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while n: # n초 동안 반복
    q = deque()
    
    # 초기 상태 : 폭탄의 위치 큐에 추가
    for i in range(r):
        for j in range(c):
            if l[i][j] == 'O':
                q.append((i, j))
    
    # '.' -> 'O'로 셋팅 -> 1초 소비
    for i in range(r):
        for j in range(c):
            if l[i][j] == '.':
                l[i][j] = 'O'
    
    n -= 1 
    
    if n == 0:
        break
    
    # 폭탄 파괴 -> 1초 소비
    while q:
        y, x = q.popleft()
        l[y][x] = '.' # 폭탄자리 파괴
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x   
            if 0 <= nx < c and 0 <= ny < r and l[ny][nx] == 'O':
                l[ny][nx] = '.' # 상하좌우도 파괴
    n -= 1

for each in l:
    print("".join(each))