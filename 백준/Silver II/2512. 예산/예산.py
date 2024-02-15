def find_max_budget(budgets, total_budget):
    left = 0
    right = max(budgets)
    result = 0    
    
    # left가 right보다 같거나 작을때까지만 반복
    while left <= right:
        # 상한액은 left+right를 2로 나눈 것
        mid = (left + right) // 2
        total = 0
        # 예산과 상한액 중 더 작은 것을 더해준다
        for budget in budgets:
            total += min(budget, mid)
        # 만약 더한 값이 국가의 총 예산보다 작다면?
        if total <= total_budget:
            # 현재 상한액을 저장 후, left 값을 옮겨서 탐색범위를 더 큰 값으로 좁힘
            result = mid
            left = mid + 1 
        else: # 더한값이 더 크다면 탐색범위를 더 작은 값으로 좁힘
            right = mid - 1
           
    return result
    
n = int(input())
budgets = []
budgets = list(map(int, input().split()))
total_budget = int(input())
maximum_budget = find_max_budget(budgets, total_budget)
print(maximum_budget)


        