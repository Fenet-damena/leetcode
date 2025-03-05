# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        s = set(nums)
        nums = list(s)
        nums.sort(reverse = True)

        if len(nums)<3:
            return max(nums)
        return nums[2]
        