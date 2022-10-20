#2798 블랙잭

N, M = map(int, input().split())
num = list(map(int, input().split()))

result = 0

for i in range(N):
    for j in range(i + 1, N):
        for z in range(j + 1, N):
            sum =num[i] + num[j] +num[z]
            if sum <= M:
                result = max(result, sum)
                
print(result)