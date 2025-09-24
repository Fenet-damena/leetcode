# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

memo = Counter()
def fib(i):
    if i ==0 or i ==1:
        return i
    if i not in memo:
        memo[i]=fib(i-1) + fib(i-2)
    return memo[i]
class Solution:
    def fib(self, n: int) -> int:
        return fib(n)