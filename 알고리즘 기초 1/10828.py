import sys

# 정수 x를 넣는 push
def push(x):
    stack.append(x)

#없으면 -1
def pop():
    if(not stack):
        return -1
    else:
        return stack.pop()

# len으로 사이즈 출력
def size():
    return len(stack)

# 스택이 비어있으면 1, 아니면 0을 출력
def empty():
    return 0 if stack else 1

# 스택의 가장 위에 있는 정수를 출력, 없으면 -1
def top():
    return stack[-1] if stack else -1

N = int(sys.stdin.readline().rstrip()) #rstrip=공백제거
stack = []

for _ in range(N):
    input_split = sys.stdin.readline().rstrip().split()

    order = input_split[0]

    if order == "push":
        push(input_split[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "empty":
        print(empty())
    elif order == "top":
        print(top())