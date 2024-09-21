

n = int(input())  # 수열의 크기
a = list(map(int, input().split()))  # 수열

dp = [1] * n  

for i in range(1, n):
    for j in range(i):  # i까지 탐색
        if a[i] > a[j]:  # 증가하는 조건
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp)) 