t = int(input())
def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True
    
def dfs(x):
    global result

    if x == n:
        result += 1
    else:
        for i in range(n):
            row[x] = i
            if check(x):
                dfs(x+1)


for tc in range(1, t + 1):
    n = int(input())
    row = [0] * n
    result = 0
    dfs(0)
    print(f"#{tc}", result)
