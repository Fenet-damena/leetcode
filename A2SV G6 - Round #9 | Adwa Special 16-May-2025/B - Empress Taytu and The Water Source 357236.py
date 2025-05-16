# Problem: B - Empress Taytu and The Water Source - https://codeforces.com/gym/601269/problem/B

from math import ceil
no_g = int(input())
t = []
for _ in range(no_g):
    n, k = map(int,input().split())
    d = list(map(int,input().split()))
    a =  list(map(int,input().split()))
    t.append((n,k,d,a))
    

    
def wagsize (no_g , t):
    ans = []
    for n, k ,d , a in t:
        left, right = 1, max(d)
        best = -1
        while left <= right:
            mid = (left + right)//2
            times = 0
            for  i in range(n):
                rq = (d[i]+mid-1)//mid
                times += rq * a[i]
            if times <= k:
                best = mid
                right = mid -1
            else:
                left = mid + 1
        ans. append(best)
    return ans
for i in wagsize(no_g,t):
    print(i)



    