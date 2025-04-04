# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)

        while i < n :
            pos = nums[i] - 1
            if nums[i] != nums[pos]:
                nums[i], nums[pos] = nums[pos], nums[i]
            else:
                i +=1
        print(nums)


        ans = []
        for i in range(n):
            if nums[i] != i+1:
                ans.append(i+1)
        return ans 

        