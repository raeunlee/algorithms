def solution(expression):
    # 3! = 6개의 경우의 수
    operations = [('+', '-', '*'), ('+', '*', '-'), ('-', '+', '*'),
                  ('-', '*', '+'), ('*', '+', '-'), ('*', '-', '+')]
    answer = []
    
    for op in operations:
        a = op[0]    # 우선순위 1 연산자
        b = op[1]    # 우선순위 2 연산자
        temp_list = []

        # 우선순위 1 연산자를 기준으로 나누기
        for e in expression.split(a):
            temp = []
            # 우선순위 2 연산자를 기준으로 나누고 괄호 씌우기
            for i in e.split(b):
                temp.append(f"({i})")  # 괄호를 정상적으로 씌움
            # 위에서 나눈 값들을 우선순위 2 연산자로 다시 연결하기
            temp_list.append(f'({b.join(temp)})')
        # 최종계산식
        result = a.join(temp_list)
        # 최댓값
        answer.append(abs(eval(result)))

    return max(answer)    # 제일 큰 값

