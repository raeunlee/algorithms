n = int(input())
arr = list(map(int, input().split()))
tmp = arr[:len(arr)-1]
result = arr[-1]

dp = [[0] * 21 for _ in range(len(tmp))]
dp[0][tmp[0]] = 1

for i in range(1, len(tmp)):
    for j in range(21):
        if dp[i-1][j] != 0:
            if j + tmp[i] <= 20:
                dp[i][j + tmp[i]] += dp[i-1][j]
            if j - tmp[i] >= 0:
                dp[i][j - tmp[i]] += dp[i-1][j]
                
print(dp[len(tmp) - 1][result])