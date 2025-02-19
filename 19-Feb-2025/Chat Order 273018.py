# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

order={}
for i in range(int(input())):
    name=input()
    if name in order:
        del order[name]
    order[name]=i
for k in list(order.keys())[::-1]:
    print(k)