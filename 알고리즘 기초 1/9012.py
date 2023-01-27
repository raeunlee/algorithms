''' 
# 스택 사용하지 않고 풀이
import sys

t = int(input())

for _ in range(t):
    input= sys.stdin.readline().rstrip()
    sum = 0
    
    for i in input:
        if i == ('('):
            sum += 1
        elif i == (')'):
            sum -= 1
        if sum < 0 :
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES') '''

# 스택 사용해서 풀이
import sys
t = int(input())

for i in range(t):
    input = sys.stdin.readline().rstrip()
    stack = []
    cnt = 0
    
    for i in input:
        if i == ('('):
            stack.append(i)
        elif i == (')'):
            if stack: #스택이 있는경우
                stack.pop()
            else: #스택이 없는경우
                print("NO")
                break
    else: 
        if not stack:
            print("YES")
        else:
            print("NO")
                
