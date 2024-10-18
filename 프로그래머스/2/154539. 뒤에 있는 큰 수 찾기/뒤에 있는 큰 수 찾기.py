def solution(numbers):
    answer = [-1] * len(numbers)
    stack = [0]

    for i in range(1, len(numbers)):
        # stack이 비어있지 않고,
        # stack의 맨위가 현재 숫자보다 크면
        while stack and numbers[stack[-1]] < numbers[i]: 
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer
    
