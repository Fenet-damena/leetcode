# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < n:
            pos = nums[i] - 1
            if nums[pos] != nums[i]:
                nums[i],nums[pos] = nums[pos], nums[i]
            else:
                i +=1
        ans = []
        for j in range(n):
            if j + 1 != nums[j]:
                ans.append(nums[j])
                ans.append(j+1)
        return ans