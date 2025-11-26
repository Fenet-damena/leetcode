# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int,input().split())
l = list(map(int,input().split()))
k = list(map(int,input().split()))
i, j = 0, 0
ans = []
while i < n and j < m:
    if l[i] < k[j]:
        ans.append(l[i])
        i += 1

    else:
        ans.append(k[j])
        j += 1 
while i< n:
    ans.append(l[i])
    i += 1  
while j < m:    
    ans.append(k[j])
    j += 1   
print(*ans)

