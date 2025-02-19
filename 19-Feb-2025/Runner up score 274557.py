# Problem: Runner up score - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    mx=max(arr)
    arr.sort()
    for i in range(len(arr)-1,-1,-1):
        if arr[i]!=mx:
            print(arr[i])
            break