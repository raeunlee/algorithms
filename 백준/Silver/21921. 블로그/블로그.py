import sys

# 입력
input = sys.stdin.readline
N, X = map(int, input().split())
visitors = list(map(int, input().split()))

max_sum = 0
count = 0
tmp_sum = sum(visitors[:X])

for i in range(N - X + 1):
    if tmp_sum == max_sum:
        count += 1
    elif tmp_sum > max_sum:
        max_sum = tmp_sum
        count = 1

    if i + X < N:
        tmp_sum = tmp_sum - visitors[i] + visitors[i + X]

# 출력
if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(count)
