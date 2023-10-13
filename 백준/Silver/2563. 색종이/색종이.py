paper = [[0]*101 for i in range(101)]

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[x+i][y+j] = 1

r = 0
for i in paper:
    r += sum(i)

print(r)