# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        tot=0
        d=Counter()
        c=0
        for i in range(len(nums)):
            tot+=nums[i]
            if tot == k:
                c+=1
            if (tot-k) in d:
                c+=d[tot-k]
         
            d[tot]+=1

        return c