# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

       def edit(s):
            stack = []
            for i in s:
                if i == "#":
                    if stack:
                        stack.pop()
                else:
                    stack .append(i)
            return stack
       if edit(s) == edit(t):
           return True
       return False
        