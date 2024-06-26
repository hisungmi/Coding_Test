import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
q = deque()
for _ in range(N):
    a = input().split()
    if a[0] == "1":
        q.appendleft(a[1])
    elif a[0] == "2":
        q.append(a[1])
    elif a[0] == "3":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif a[0] == "4":
        if q:
            print(q.pop())
        else:
            print(-1)
    elif a[0] == "5":
        print(len(q))
    elif a[0] == "6":
        if q:
            print(0)
        else:
            print(1)
    elif a[0] == "7":
        if q:
            print(q[0])
        else:
            print(-1)
    elif a[0] == "8":
        if q:
            print(q[-1])
        else:
            print(-1)