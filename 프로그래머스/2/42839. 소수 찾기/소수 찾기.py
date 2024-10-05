from itertools import permutations
import math

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
    
        
def solution(numbers):    
    tmp = list(numbers)
    print(tmp)
    l = []
    
    for i in range(1, len(tmp) + 1):
        for comb in permutations(tmp, i):
            now = ''.join(comb)
            l.append(now)
    
    print(set(l))
    
    count = 0
    
    for each in set(l):
        if each[0] == '0': continue
        else:
            print(each)
            if isPrime(int(each)) == True:
                count += 1
    return count