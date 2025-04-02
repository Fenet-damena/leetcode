# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m=max(nums)
    
        s=set((nums))
        for i in range(m+2):
            if i not in s:
                return i
        