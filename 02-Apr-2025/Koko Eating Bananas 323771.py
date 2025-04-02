# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans = -1
        def helper(speed):
            speeds = 0
            for i in piles:
              speeds += ceil(i/mid)
            return speeds

        low ,high = 1, max(piles)
        while low <= high:
            mid = (low + high)// 2
            if helper(mid) > h:
                low = mid +1
            else:
                high = mid - 1
                ans = mid
        return ans