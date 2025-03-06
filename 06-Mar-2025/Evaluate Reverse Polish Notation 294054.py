# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = "+/-*"

        for i in tokens:
            if  i not in operations:
                stack.append(i)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if i == "+":
                    stack.append(a+b)
                elif i == "*":
                    stack.append(a*b)
                elif i == "/":
                    stack.append(a/b)
                else:
                    stack.append(a-b)
        return int(stack[0])
                
                

        