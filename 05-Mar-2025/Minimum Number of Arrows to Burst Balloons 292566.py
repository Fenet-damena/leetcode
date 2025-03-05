# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sor = sorted(points,key = lambda x:x[1])
        ans = 1
        burst = sor[0][1]
        if len(points) == 0:
            return 0
        for i in range(1,len(points)):
            if burst <sor[i][0]:
                ans += 1
                burst = sor[i][1]
        return ans