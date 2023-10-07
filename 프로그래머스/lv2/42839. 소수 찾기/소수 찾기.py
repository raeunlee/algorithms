from itertools import permutations
import math

def solution(numbers):
    answer = []
    numbers_to_list = list(numbers)
    # print(numbers_to_list)
    permutation = []
    for i in range(1, len(numbers)+1):
        permutation += list(permutations(numbers, i))
        #print(permutation)
    
    new_nums = [int(("").join(p)) for p in permutation] 
    #print(new_nums)
    
    for n in new_nums:                            
        if n < 2:                                 
            continue
        check = True            
        for i in range(2,int(math.sqrt(n)) + 1):        
            if n % i == 0:                        
                check = False
                break
        if check:
            answer.append(n)

    return len(set(answer))
                
                
            
   