# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        memo = {}

        def dp(i):
            if i >= l:
                return 0
            if i  in memo:
                return memo[i]

                
            ones = cost[i] + dp(i+1)
            twos = cost[i] +dp(i+2)
            memo[i] = min(ones, twos)
            return memo[i]
        return min (dp(0),dp(1))
            

        