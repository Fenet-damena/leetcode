# Problem: Find the Middle Index in Array - https://leetcode.com/problems/find-the-middle-index-in-array/

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        tot=sum(nums)
        ps=0
        for i in range(len(nums)):
            if ps==(tot-ps-nums[i]):
                return i
            ps+=nums[i]
        return -1
        