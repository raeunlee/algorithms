#백준 피보나치 수 5

n = int(input())

def recur(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return recur(num-1) + recur(num-2)
        
print(recur(n))