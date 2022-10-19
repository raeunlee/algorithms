### 내장함수 sorted 사용
import sys
input=sys.stdin.readline

n=int(input())
list1=[]

for i in range(n):
    list1.append(int(input()))

for i in sorted(list1):
    print(i)