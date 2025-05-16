# Problem: A - Escaping Prison - https://codeforces.com/gym/601269/problem/A

for j in range(int(input())):
    n, h = map(int,input().split())
    ll =[]
    for i in range(n):
        l,w = map(int,input().split())
        ll.append([l,w])
    cur = 0
    for i,j  in ll:
        if i >j:
            cur += i
        else:
            cur += j
    if cur >= h:
        print("YES")
    else:
        print("NO")


