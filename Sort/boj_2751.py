# 2751 수 정렬하기 2

#n = int(input())
#list1 = []
#for i in range(n):
#    list1.append(int(input()))
#    list1.sort()
#for j in list1:
#    print(j)

#시간초과로 실패 ㅋㅋ




### 내장함수 sorted 사용
import sys
input=sys.stdin.readline

n=int(input())
list1=[]

for i in range(n):
    list1.append(int(input()))

for i in sorted(list1):
    print(i)