# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l ,r = 1 ,max(piles)
        while l<=r:

            mid = (r+l)//2
            cal = 0
            for i in piles:
                cal += ceil(i/mid)
            if cal <=h:
                r = mid - 1
                best = mid
            else:
                l = mid + 1
        return best
           