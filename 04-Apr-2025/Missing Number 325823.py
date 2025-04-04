# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)

        while i< n:
            pos = nums[i]
            if nums[i] < n and nums[i] != nums[pos]:
                nums[i], nums[pos] = nums[pos],nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i:
                return i
        return n