# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        s = sum(nums)
  
        if s % 2 != 0:
            return False
        
        target = s // 2
        n = len(nums)
        
        dp = [False] * (target + 1)
        dp[0] = True  
        
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]
