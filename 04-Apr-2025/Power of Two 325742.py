# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def pow2(n):
            if n == 1:
                return True
                
            elif n < 1 or n % 2 !=0:
                return False
            else:
                return pow2(n//2)
        return pow2(n)
              