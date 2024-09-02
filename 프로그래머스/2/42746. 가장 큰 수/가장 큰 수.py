def solution(numbers):
    l = []
    for number in numbers:
        l.append(str(number))
    # print(l)
    l.sort(key=lambda x: x*3, reverse=True)
    answer = ''
    return str(int(''.join(l)))