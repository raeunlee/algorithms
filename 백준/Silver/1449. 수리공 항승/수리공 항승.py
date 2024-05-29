
# 물이새는곳 n, 테이프의 길이 l
n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

start = arr[0]
count = 1
dist = 0
for i in range(1, n):
    dist += abs(arr[i] - arr[i-1])
    if l > dist: 
        continue
    else:
        count += 1
        dist = 0
print(count)