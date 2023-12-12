n = int(input()) #계단 개수	
s=[int(input()) for _ in range(n)] # 계단 리스트

dp = [0] * n #dp

if len(s) <= 2:
    print(sum(s))
else: #계단이 3개 이상
    dp[0] = s[0] # 첫째 계단
    dp[1] = s[0] + s[1] #첫쨰 + 둘째 계단
   
    for i in range(2, n):
        dp[i]=max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])

    print(dp[-1])