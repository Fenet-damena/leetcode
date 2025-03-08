# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

def power(n):
    if n < 1:
        return False
    elif n == 1:
        return True
    elif n % 4 != 0: 
        return False
    else:
        return  power(n//4)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return power(n)
        