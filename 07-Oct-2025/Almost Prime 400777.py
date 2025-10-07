# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

from collections import Counter
 
 
n = int(input())
def check(n):
    fact = Counter()
 
    d = 2
 
    while d*d <= n:
        while n % d == 0:
                fact [d] += 1
                n //= d
        d += 1
    if n>1:
        fact[n] += 1
    return len(fact)
 
 
c = 0
for i in range(1, n+1):
    if check(i) == 2:
        c += 1
print(c)