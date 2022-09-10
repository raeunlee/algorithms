#25304 영수증 문제 

#첫째 줄에는 영수증에 적힌 총 금액 X
x = int(input())
#둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N
n = int(input())

sum = 0 
#N개의 줄에는 각 물건의 가격 a와 개수 b가 공백을 사이에 두고 주어짐
for i in range(n):
    a,b = map(int,input().split())
    sum += a*b
#구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 yes, 아니면 no
if x == sum: 
    print("Yes")
else:
    print("No")
