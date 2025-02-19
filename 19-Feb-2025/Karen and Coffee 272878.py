# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

from collections import defaultdict

n, k, q = map(int, input().split())
rec = []
for _ in range(n):
    ll, r = map(int, input().split())
    rec.append([ll, r])

quer = []
for _ in range(q):
    lf, r = map(int, input().split())
    quer.append([lf, r])

prifix = [0] * (200000 + 2)

for s, e in rec:
    prifix[s] += 1
    if e + 1 < len(prifix):
        prifix[e + 1] -= 1

for i in range(1, len(prifix)):
    prifix[i] += prifix[i - 1]

for i in range(len(prifix)):
    if prifix[i] >= k:
        prifix[i] = 1
    else:
        prifix[i] = 0  

for i in range(1, len(prifix)):
    prifix[i] += prifix[i - 1]

for s, e in quer:
    if s > 0:  
        an = prifix[e] - prifix[s - 1]
    else:
        an = prifix[e]  
    print(an)