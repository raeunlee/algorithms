n = int(input())

count = 1
stack = []
op = []

for i in range(n):
    data = int(input())

    while count <= data:
        stack.append(count)
        op.append('+')
        count += 1

    if stack.pop() == data:
        op.append('-')

    else:
        print("NO")
        exit(0)
result = '\n'.join(op)
print(result)
