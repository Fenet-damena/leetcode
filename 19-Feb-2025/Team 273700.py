# Problem: Team - https://codeforces.com/contest/231/problem/A

n=int(input())
c=0
for i in range(n):
    p,v,t=map(int,input().split())
    a=p+v+t
    if a>=2:
        c+=1
print (c)

    