# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i ==0:
                return nums[0]
            if i == 1:
                return max(nums[0],nums[1])
            if i in memo:
                return memo[i]
            rob = dp(i-2) + nums[i]
            not_rob = dp(i-1)
            memo[i] = max(rob, not_rob)
            return memo[i]
        return dp(len(nums)-1)
                
        