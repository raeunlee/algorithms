# 분해합

# 198 -> 216 으로 가는 분해합은 알겠는데, 역으로는?
# 자리수 더하기: 숫자를 문자열로 바꾸고 한자리씩 int로 리스트에 저장



n= int(input())
ans = 0

for i in range(1, n+1):
    A = list(map(int, str(i)))
    ans = i + sum(A)
    
    if ans == n:
        print(i)
        break
    if i == n:
        print(0)



