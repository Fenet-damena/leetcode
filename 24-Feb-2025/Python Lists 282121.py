# Problem: Python Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    lists = []
    
    for _ in range(N):
        command = input().split()
        if command[0] == "insert":
            lists.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(lists)
        elif command[0] == "append":
            lists.append(int(command[1]))
        elif command[0] == "remove":
            lists.remove(int(command[1]))
        elif command[0] == "sort":
            lists.sort()
        elif command[0] == "pop":
            lists.pop()
        else:
            if command[0] == "reverse":
               lists = lists[::-1]
        
        
            