#백준 제로 10773

import sys
k = int(input())
stack = []

for i in range(k):
    input = sys.stdin.readline().rstrip()
    n = int(input)
    
    if n == 0:
        stack.pop()
       
    else:
        stack.append(n)
    
print(sum(stack))