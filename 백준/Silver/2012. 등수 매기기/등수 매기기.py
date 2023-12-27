# 등수 매기기  

n = int(input())
l = []
for i in range(n):
    l.append(int(input())) 
l.sort()
x = 0
for i in range(n):
    x += abs(i+1 - l[i])

print(x)
    