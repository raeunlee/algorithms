n, k = map(int, input().split())
# 주어지는 무게를 저장하는 배열
things = [(0,0)]

for _ in range(n):
    w, v = map(int, input().split())
    things.append((w, v))

# 풀이한 표와 같은 양식의 2중 배열
dp = [[0] * (k + 1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        w, v = things[i]
        if w > j:
            dp[i][j] = dp[i-1][j]   
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)            
            
print(dp[n][k])