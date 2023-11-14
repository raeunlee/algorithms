def solution(s):
    stack = []
    for x in s:
        if x == '(': # 여는 괄호면 append 
            stack.append(x)
        else: # 닫는 괄호면 
            if stack == []: #비어있는데 나오면 False
                return False
            else: #아니라면 pop
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False