# 백준 점프
n = int(input())

jump = []
for i in range(n):
    jump.append(list(map(int, input().split())))
    
dp = [[0] * n for i in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            print(dp[i][j])
            break
        now = jump[i][j]
        
        if i + now < n:
            dp[i+now][j] += dp[i][j]
        
        if j + now < n:
            dp[i][j+now] += dp[i][j]
            
    
        
    
    


