#피아노체조 
import sys
input = sys.stdin.readline
n = int(input())
nl = list(map(int, input().split()))
mis = [0] * n
for i in range(1, n):
    if nl[i-1] > nl[i]: # 전꺼가 더 크다면 
        mis[i] = mis[i-1] + 1 # mis[i]는 전의 실수 + 1
    else: 
        mis[i] = mis[i-1] # 아니라면 직전것과 같은 실수
        
q = int(input())
for j in range(q):
    x, y = map(int,input().split())
    print(mis[y-1] - mis[x-1]) 
            