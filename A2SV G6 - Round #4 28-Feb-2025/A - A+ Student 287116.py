# Problem: A - A+ Student - https://codeforces.com/gym/590053/problem/A

for i in range(int(input())):
    a,b,c =map(int,input().split())
    mx  = max(a,b,c)
    if a==b==c:
          b1 = mx-b+1
          a1 = mx-a+1
          c1 = mx-c+1
    elif a==b ==mx or a==c==mx or b==c==mx:
          b1 = mx-b+1
          a1 = mx-a+1
          c1 = mx-c+1

    elif a == mx:
        a1 = 0
        b1 = mx-b+1
        c1 = mx-c+1
    elif b == mx:
        b1 = 0
        c1 = mx-c+1
        a1 = mx-a+1
    elif c == mx:
            c1 =0
            b1 = mx-b+1
            a1 = mx-a+1
    else:
            b1 = mx-b+1
            a1 = mx-a+1
            c1 = mx-c+1
         
         
    print(a1,b1,c1)



    
