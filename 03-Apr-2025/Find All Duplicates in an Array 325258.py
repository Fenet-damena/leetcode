# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < n:
            pos = nums[i] - 1
            if nums[pos] != nums[i]:
                nums[pos], nums[i] = nums[i], nums[pos]
            else:
                i +=1
        ans = []
        print(nums)

        for j in range(n):
            if nums[j] != j + 1:
                ans.append(nums[j])
        return ans