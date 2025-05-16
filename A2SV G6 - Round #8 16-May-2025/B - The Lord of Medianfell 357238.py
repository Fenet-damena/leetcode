# Problem: B - The Lord of Medianfell - https://codeforces.com/gym/599383/problem/B

for i in range(int(input())):
    n, s= map(int,input().split())
    maxm = s//(n//2 +1 )
    print(maxm)