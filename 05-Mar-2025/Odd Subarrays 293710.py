# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

for i in range(int(input())):
    n = int(input())
    num = list(map(int,input().split()))
    ans = 0

    left = 0
    while left+1 < n:
        if num[left] > num[left+1]:
            ans += 1
            left +=1
        left +=1
    print(ans)
       
