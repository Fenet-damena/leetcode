# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        ans = 0
        
        for house in houses:
            idx = bisect.bisect_left(heaters, house)

            l_dis = float('inf') if idx == 0 else house - heaters[idx - 1]
            r_dis= float('inf') if idx == len(heaters) else heaters[idx] - house
            
            ans = max(ans, min(l_dis,r_dis))
        
        return ans

        