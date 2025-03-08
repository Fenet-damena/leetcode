# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

def fb(n):
    if n <= 1:
            return n
    else:
            return fb(n-1) + fb(n-2)
            
class Solution:
    def fib(self, n: int) -> int:
        return fb(n)
        
        