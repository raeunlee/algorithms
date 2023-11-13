def solution(n):
  
    x = list(str(n))
    x.sort(reverse=True)
    ans = int("".join(x))
    return ans