# 10866 덱

import sys
from collections import deque

deck=deque()

def push_front(X):
    deck.appendleft(X)

def push_back(X):
    deck.append(X)

def pop_front():
    if deck:
        print(deck.popleft())
    else:
        print(-1)

def pop_back():
    if deck:
        print(deck.pop())
    else:
        print(-1)

def size():
    print(len(deck))

def empty():
    if deck:
        print(0)
    else:
        print(1)

def front():
    if deck:
        print(deck[0])
    else:
        print(-1)

def back():
    if deck:
        print(deck[-1])
    else:
        print(-1)
        

N = int(sys.stdin.readline().rstrip())
for i in range(N):
    input_split = sys.stdin.readline().rstrip().split()
    order = input_split[0]
    
    if order == 'push_front':
        push_front(input_split[1])
    elif order == 'push_back':
        push_back(input_split[1])
    elif order == 'pop_front':
        pop_front()
    elif order == 'pop_back':
        pop_back()
    elif order == 'size':
        size()
    elif order == 'empty':
        empty()
    elif order == 'front':
        front()
    elif order == 'back':
        back()
    else:
        break
    