import heapq
n = int(input())
q = []
for i in range(n):
    s, t = map(int, input().split())
    q.append([s,t])
q.sort() # 시작 시간이 빠른 순서대로 일단 정렬

room = []
# 맨처음 시작하는 수업의 종료시간을 넣어줌
heapq.heappush(room, q[0][1])

for i in range(1,n):
    if q[i][0] < room[0]: # 기존 수업의 종료시간이 시작시간보다 더 크다면?
        heapq.heappush(room, q[i][1]) # 새로운 방을 하나 더 만든다
    else:
        heapq.heappop(room) # 기존 수업의 종료시간이 시작시간보다 같거나 작다면, 원래 수업을 빼준다
        heapq.heappush(room, q[i][1]) # 그리고 현재 수업의 종료시간을 넣어준다

print(len(room))
# heapq는 작은 수 부터 정렬됨.