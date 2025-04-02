# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def Days(cap):
            day = 1
            currt_w = 0
            for i in weights:
                if  i >  cap:
                    return float('inf')
                
                if currt_w + i > cap:
                    day += 1
                    currt_w = 0
                currt_w += i
            return day

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
                
