# 1021 회전하는 큐
from collections import deque

#연산들 정리
def first():
    make_q.append(idx.popleft())
def second():
    idx.append(idx.popleft())
    
def third():
    idx.appendleft(idx.pop())
    

idx=deque(list())
N,M = map(int, input().split())
for i in range(N):
    idx.append(i)
print(idx)
#기본적으로 주어지는 큐

want_q = deque(list(map(int, input().split()))) #뽑을 큐
print(want_q)

make_q = deque(list())

while idx:
    cnt = 0
    if want_q:
        if idx[0] == want_q[0]:
            first() #주어지는 큐의 첫번째 수와, 뽑으려는 큐의 첫번째 수가 같으면 pop
            want_q.popleft() #뽑기 리스트에서 popleft
            continue
        else:
            if idx[want_q[0]]/2 < len(idx):
                second()
                cnt += 1
            elif idx[want_q[0]]/2 > len(idx):
                third()
                cnt += 1
            else:
                second()
                cnt += 1
    else:
        break
print(cnt)
            