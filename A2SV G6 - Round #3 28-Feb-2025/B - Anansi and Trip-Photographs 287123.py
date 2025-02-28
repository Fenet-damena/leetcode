# Problem: B - Anansi and Trip-Photographs - https://codeforces.com/gym/588468/problem/B

for i in range(int(input())):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    m=len(l)//2
    l1=l[:m]
    l2=l[m:]
    t=True
    for i in range(len(l1)):
        if l2[i]-l1[i]<x:
            t=False
            break
    if t:
        print("YES")
    else:
        print("NO")
    