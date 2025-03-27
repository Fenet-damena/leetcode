# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def Days(capacity):
            load = 0
            D = 1
            for weight in weights:
                if weight > capacity:
                    return float('inf')
                if load + weight > capacity:
                    D += 1
                    load = 0
                load += weight
            return D
        
        left, right = 0, sum(weights)
        ans = right
        while left <= right:
            mid = (left+right) // 2
            if Days(mid) > days:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1
        return ans
                
