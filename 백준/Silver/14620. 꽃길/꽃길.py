n = int(input())
flower = []
for i in range(n):
    row = list(map(int, input().split()))
    flower.append(row)
    
dir = [(0,0), (-1,0), (1,0), (0,-1), (0,1)]
visited =[[False] * n for _ in range(n)]
answer = 1e15
def check(y,x):
    global n
    for dy, dx in dir:
        ny = y + dy
        nx = x + dx
        #범위 넘어갔거나 방문했으면
        if 0 > ny or ny > n-1 or 0>nx or nx > n-1 or visited[ny][nx]:
            return False
    return True

def calculate(y,x):
    global n
    result = 0
    for dy, dx in dir:
        ny = y + dy
        nx = x + dx
        result += flower[ny][nx]
    return result
            

def dfs(x, cost, cnt):
    global answer
    if cnt == 3:
        answer = min(answer, cost)
        return
    for i in range(x, n):
        for j in range(1, n):
            if check(i,j):
                visited[i][j] = True
                for dy, dx in dir:
                    visited[i+dy][j+dx] = True
                dfs(i, cost + calculate(i,j), cnt+1)
                visited[i][j] = False
                for dy, dx in dir:
                    visited[i+dy][j+dx] = False

dfs(1,0,0)
print(answer)