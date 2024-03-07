def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        row = []
        for j in range(len(arr2[0])):
            row.append(0)
        answer.append(row)

    
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += (arr1[i][k] * arr2[k][j])


    print(answer)
    
    
    
    
    return answer