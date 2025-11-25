# Problem: A - Drawing D - https://codeforces.com/gym/653030/problem/A

n = int(input())

mid = n // 2 

for i in range(n):
    leng = abs(mid - i)
    Ds= n - 2 * leng
    starts = leng
    ans = '*' * starts + 'D' * Ds+ '*' * starts
    print(ans)
