#알파벳 골

r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]
ans = 0
visited=[0]*26 #알파벳은 총 26개

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x, y, count):
    global ans
    ans = max(ans, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<r and 0<=ny<c and visited[ord(arr[nx][ny])-ord('A')]==0:
            visited[ord(arr[nx][ny]) - ord('A')] = 1
            dfs(nx, ny, count+1)
            visited[ord(arr[nx][ny]) - ord('A')] = 0

visited[ord(arr[0][0]) - ord('A')] = 1
dfs(0,0,1)
print(ans)