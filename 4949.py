import sys

while True:
    input = str(sys.stdin.readline().rstrip())
    stack = []
    
    if input == '.':
        break
    
    for i in input:
        if i == ('(') or i == ('['):
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i) 
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)  
                break
            
    if not stack:
        print('yes')
    else:
        print('no')