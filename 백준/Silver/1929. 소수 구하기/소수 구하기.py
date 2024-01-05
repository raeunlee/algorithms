# 소수 구하기
import math

m, n = map(int, input().split())

for i in range(m, n+1):
    if i==1:#1은 소수가 아니므로 제외
        continue
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0: #제곱근으로 나누어 떨어지면
            break
    else:
        print(i)
            
    
