import sys
input = sys.stdin.readline
n = int(input())
xy = []
for i in range(n):
    x, y = map(int, input().split())
    xy.append([x,y])

xy.sort(key=lambda x: (x[0] , x[1]))

for i in xy:
    print(*i)