import sys

t = int(input())

for _ in range(t):
    input= sys.stdin.readline().rstrip()
    sum = 0
    
    for i in input:
        if i == ('('):
            sum += 1
        elif i == (')'):
            sum -= 1
        if sum < 0 :
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')
            
    
    
    
 
#    if input[0] == ('('):
#        if input.count('(') == input.count(')'):
#            if input[-1] == (')'): print('YES')
#            else: print('NO')
#        else: print('NO')
#    else:
#        print('NO')
            