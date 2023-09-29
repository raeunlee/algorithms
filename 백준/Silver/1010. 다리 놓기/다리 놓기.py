import math
T = int(input())

for i in range(T):
    n, m = map(int,input().split())
    c = math.comb(m , n)
    print(c)

    

