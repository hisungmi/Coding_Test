import sys
while True:
    input = sys.stdin.readline
    a, b = map(int, input().split())
    if a + b != 0:
	    print(a + b)
    else:
        break