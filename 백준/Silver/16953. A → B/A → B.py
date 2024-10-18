a,b = map(int, input().split())

def dfs(now,count, visited):
    
    if now == b:
        return count
    
    if now > b or now in visited:
        return -1
    
    visited.add(now)
    
    x = dfs(now * 2, count+1, visited)
    y = dfs(int(str(now) + "1"), count + 1, visited)

    if x != -1:
        return x
    if y != -1:
        return y
    
    return -1
visited = set()
result = dfs(a, 1, visited)
print(result)
    
