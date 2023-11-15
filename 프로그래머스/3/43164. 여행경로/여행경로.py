from collections import deque

def dfs(tickets, path):
    if not tickets:  # 모든 티켓을 사용한 경우
        return path
    current = path[-1]
    for i, ticket in enumerate(tickets):
        if current == ticket[0]:
            next_tickets = tickets[:i] + tickets[i+1:]  # 사용한 티켓을 제외한 리스트
            next_path = dfs(next_tickets, path + [ticket[1]])
            if next_path:
                return next_path
    return None

def solution(tickets):
    tickets.sort()  # 알파벳 순서로 정렬
    answer = dfs(tickets, ["ICN"])
    return answer

