# Problem: A - Nth Digit in Sequence - https://codeforces.com/gym/588468/problem/A

n=int(input())
s=""
for i in range(1,n+1):
    s+=str(i)
print(s[n-1])
    
