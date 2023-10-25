def solution(survey, choices):
    answer = ''
    mydict = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    for i in range(len(survey)):
        if choices[i] > 4:
            mydict[survey[i][1]] += choices[i]-4
        elif choices[i] < 4:
            mydict[survey[i][0]] += (choices[i]-4)*(-1)
        else:
            continue
            
    print(mydict)
    
    if mydict.get('R') > mydict.get('T'):
        answer += 'R'
    elif mydict.get('R') < mydict.get('T'):
        answer += 'T'
    else:
        answer += 'R'
    
    if mydict.get('C') > mydict.get('F'):
        answer += 'C'
    elif mydict.get('C') < mydict.get('F'):
        answer += 'F'
    else:
        answer += 'C'
        
    if mydict.get('J') > mydict.get('M'):
        answer += 'J'
    elif mydict.get('J') < mydict.get('M'):
        answer += 'M'
    else:
        answer += 'J'
        
    if mydict.get('A') > mydict.get('N'):
        answer += 'A'
    elif mydict.get('A') < mydict.get('N'):
        answer += 'N'
    else:
        answer += 'A'

    return answer