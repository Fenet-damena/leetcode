# Problem: A - The Mad King's Calls - https://codeforces.com/gym/599383/problem/A

for i in range(int(input())):
    n = input()
    b = int(n[0])-1
    k = b*10
    for i in range(1,len(n)+1):
        k += i
    print(k)