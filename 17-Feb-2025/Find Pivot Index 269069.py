# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ps=0
        s=0
        for num in nums:
            s+=num
        for i  in range(len(nums)):
            if ((ps==(s-ps-nums[i]))):
                return i
            ps+=nums[i]
        return -1