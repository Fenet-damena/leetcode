# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fac(n):
            if n < 1:
                return 1

            fc = n * fac(n-1)
            return fc
        x = (fac(n))

        ans = 0
        while x%10 == 0:
            ans += 1
            x = x// 10
            
        return ans
        
        