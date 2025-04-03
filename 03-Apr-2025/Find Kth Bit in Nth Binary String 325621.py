# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def f(n, k):
            m = 2**(n-1)
            if n == 1: return "0"
            if k == m: return "1"
            return f(n-1, k) if k < m else str(1 - int(f(n-1, 2*m - k)))
        return f(n, k)
        