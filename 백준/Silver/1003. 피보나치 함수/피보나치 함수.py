# 피보나치 함수
T = int(input())

for i in range(T):
    count_zero = [1,0]
    count_one = [0,1]
    N = int(input())
    if N >= 2:
        for i in range(N-1):
            count_zero.append(count_one[-1])
            count_one.append(count_zero[-2] + count_one[-1])
    print(count_zero[N], count_one[N])
            
