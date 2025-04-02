# Problem: Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        l = 0
        h = len(nums)-1

        while l <= h:
            if nums[l] < nums[h]:
                return min(ans, nums[l])
            mid = (l+h) // 2
            ans = min(ans ,nums[mid])
            if nums[mid] >= nums[l]:
                l = mid +1
            else:
                h -=1
        return ans

