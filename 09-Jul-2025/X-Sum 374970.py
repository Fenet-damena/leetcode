# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

for _ in range(int(input())):
    n,m = map(int,input().split())
    b = [list(map(int,input().split())) for i in range(n)]

    d1 = {}
    d2 = {}

    for i in range(n):
        for j in range(m):
            d1[i-j] = d1.get(i-j, 0) + b[i][j]
            d2[i+j] = d2.get(i+j, 0) + b[i][j]
    ans = 0
    for i in range(n):
        for j in range(m):
            ans = max(ans, d1[i-j] + d2[i+j] - b[i][j])
    print(ans)
