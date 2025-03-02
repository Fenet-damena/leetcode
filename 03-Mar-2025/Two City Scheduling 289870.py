# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        leng = len(costs)// 2
        costs.sort(key = lambda x: x[0]-x[1])
        ans = 0
 
        for i in range(leng):
            ans += costs[i][0]
        for i in range(leng,len(costs)):
            ans += costs[i][1]
        return ans

            
            
     
