# 1021 회전하는 큐
from collections import deque

idx=deque(list())
N,M = map(int, input().split())

want_q = deque(list(map(int, input().split()))) #내가 뽑을 큐

# print("want_q", list(want_q))

# 주어지는 큐
for i in range(1, N+1):
    idx.append(i)
# print(idx)
 
#연산들 정리
def first():
    idx.popleft()
    want_q.popleft() #뽑을 큐에서 popleft
def second():
    idx.append(idx.popleft())
    #print(idx)
def third():
    idx.appendleft(idx.pop())
    #print(idx)
count = 0  
while True:
    if want_q:
        if idx[0] == want_q[0]:
            first() #주어지는 큐의 첫번째와, 뽑으려는 큐의 첫번째가 같으면 pop
        else:
            if idx.index(want_q[0]) <= len(idx)/2:
                second()
                count += 1
            elif idx.index(want_q[0]) > len(idx)/2:
                third()
                count += 1
    else:
        break


print(count)
            