# Problem: B - Delete from the Left - https://codeforces.com/gym/653030/problem/B

s = input().strip()
t = input().strip()
i, j = len(s) - 1, len(t) - 1
c = 0

while i >= 0 and j >= 0 and s[i] == t[j]:
    c += 1
    i -= 1
    j -= 1
ans= (len(s) - c) + (len(t) - c)
print(ans)
