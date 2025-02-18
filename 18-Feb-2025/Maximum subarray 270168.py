# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx=nums[0]
        cur=0
        for i in range(len(nums)):
            if cur<0:
                cur=0
            cur+=nums[i]
            mx=max(mx,cur)
        return mx
  