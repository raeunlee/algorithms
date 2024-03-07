# 블로그2
import sys
input = sys.stdin.readline

n = int(input())
col = list(input().rstrip())
d = {'B': 0, 'R':0}
pre = ''
for c in col:
    if c != pre:
        d[c] += 1
    pre = c
    
if d['B'] > d['R']:
    cnt = d['R'] + 1
else:
    cnt = d['B'] + 1
print(cnt)