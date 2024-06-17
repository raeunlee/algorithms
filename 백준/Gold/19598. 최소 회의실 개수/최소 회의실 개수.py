import heapq

n = int(input())
arr = []

for i in range(n):
    a,b = map(int, input().split())
    arr.append([a,b])
arr.sort(key=lambda x:(x[0],x[1]))

ans = []
for a, b in arr:
    if len(ans) == 0:
        heapq.heappush(ans,b)
    else:
        if ans[0] <= a:
            heapq.heappop(ans)
            heapq.heappush(ans,b)
        else:
            heapq.heappush(ans,b)
print(len(ans))