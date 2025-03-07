# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = []
        ans = 0
        num = 0

        for i in s:
            if i == "(":
                stack.append(0)
            else:
                n = stack.pop()
                if n == 0:
                    num = 1
                else:
                    num = 2 * n
                if not stack:
                    ans  += num
                else:
                    stack[-1] += num
        return ans 
            
        