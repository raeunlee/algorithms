def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        x = array[commands[i][0]-1:commands[i][1]]
        x.sort()
        answer.append(x[commands[i][2]-1])
        #print(x[commands[i][2]-1])
        
    return answer