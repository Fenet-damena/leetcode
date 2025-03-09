# Problem: B - Fix the Forecast! - https://codeforces.com/gym/591928/problem/B

for _ in range(int(input())):
    n, k = map(int, input().split())  
    a = list(map(int, input().split()))  
    b = list(map(int, input().split()))  

    indexed_a = sorted(enumerate(a), key=lambda x: x[1])
    b.sort()  

    result = [0] * n

    for i in range(n):
        original_index = indexed_a[i][0]
        result[original_index] = b[i]
    print(" ".join(map(str, result)))
