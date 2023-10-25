def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    aa = 0
    bb = 0
    cc = 0
    print(a [ (10 + 1) %  8 -1])
    for i in range(len(answers)):
        if a[(i + 1) % len(a) - 1] == answers[i]:
            aa += 1
        if b[(i + 1) % len(b) - 1] == answers[i]:
            bb += 1
        if c[(i + 1) % len(c) - 1] == answers[i]:
            cc += 1
    
    dict = {'1' : aa, '2': bb, '3':cc}
    
    max = 0
    for items in dict:
        if dict[items] >= max:
            if dict != 0:
                max = dict[items]
            
    for items in dict:
        if dict[items] == max:
            if items == '1':
                answer.append(1)
            if items == '2':
                answer.append(2)
            if items == '3':
                answer.append(3)
            
    return answer