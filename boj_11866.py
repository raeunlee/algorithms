from collections import deque
n, k = (map(int, input().split()))

yosep = deque()
yosep_answer = []



for i in range(1, n+1):
    yosep.append(i)

for j in range(n): #n번 연산을 반복해야함
    yosep.rotate(-k+1)
    if yosep:
        yosep_answer.append(yosep.popleft())
        #yosep.popleft()
        # yosep_answer.append(yosep.popleft())
    # print(yosep)
    
print("<", end='')
print( *yosep_answer,sep=', ', end='' )
print(">")