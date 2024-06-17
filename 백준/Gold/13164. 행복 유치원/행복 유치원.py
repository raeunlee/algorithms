n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = []


# 1 3 5 6 10 = > 2 2 1 4
# 4 2 2개를 제외한 2개 2 + 1 = 3이 답
# 즉, n - k 개!!!

for i in range(1, n):
    # 인접한 아이들의 차이를 구해준다 (총 n-1개)
    ans.append(arr[i] - arr[i-1])

ans.sort()

print(sum(ans[:n-k]))