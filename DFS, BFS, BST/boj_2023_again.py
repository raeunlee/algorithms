import sys
input = sys.stdin.readline

n = int(input())

def isprime(n):
    for i in range(2,n/2+1):
        if n % i == 0 :
            return False
    return True

def DFS(x):
    i