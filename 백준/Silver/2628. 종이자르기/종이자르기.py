n, m = map(int, input().split())
gatsu = int(input())

x_tmp = [0, n]
y_tmp = [0, m]

for i in range(gatsu): 
    a, b = map(int, input().split())
    if a == 0:
        y_tmp.append(b)
    elif a == 1:
        x_tmp.append(b)
        
x_tmp.sort()
y_tmp.sort()

result = 0

for i in range(len(x_tmp)-1):
    for j in range(len(y_tmp)-1):
        x = x_tmp[i+1] - x_tmp[i]
        y = y_tmp[j+1] - y_tmp[j]
        result = max(result, x*y)

print(result)