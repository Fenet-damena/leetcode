# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        ans = 0
        while low <= high:
            mid= (low + ((high-low)//2))
            if mid** 2 < x:
                low = mid +1
                ans = mid
            elif mid ** 2 > x:
                high = mid -1
                
            else:
                return mid
        return ans
        