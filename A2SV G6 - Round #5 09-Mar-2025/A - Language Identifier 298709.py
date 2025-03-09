# Problem: A - Language Identifier - https://codeforces.com/gym/591928/problem/A

for i in range(int(input())):
    x = input()
    n= len(x)
    if x[n-2:] == "po":
        print("FILIPINO")
    elif x[n-4:] == "desu" or x[n-4:] == "masu":
        print("JAPANESE")
    else:
        if x[n-5:] == "mnida":
            print("KOREAN")