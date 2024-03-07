#일곱난쟁이

import sys
from itertools import combinations

input = sys.stdin.readline

arr = []
for i in range(9):
    arr.append(int(input()))

comb = list(combinations(arr,7))
ans = []
for c in comb:
    if sum(c) == 100:
        ans = list(c)
        break
ans.sort()
for a in ans:
    print(a)