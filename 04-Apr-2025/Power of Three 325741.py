# Problem: Power of Three - https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def power3(n):
            if n ==  1:
                return True
            
            elif n <= 0 or n % 3 != 0:
                return False

            
            else:
                return power3(n//3)
        return power3(n)
        