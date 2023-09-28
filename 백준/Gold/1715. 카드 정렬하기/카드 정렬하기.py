import heapq
n = int(input())

heap = []

for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

ans = 0

while len(heap)!= 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    sum_onetwo = one + two
    ans += sum_onetwo
    heapq.heappush(heap, sum_onetwo)
print(ans)
    