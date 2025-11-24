# Problem: Find the Power of K-Size Subarrays II - https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k > n:
            return []
        if k == 1:
            return nums[:]

        ans = [-1] * (n - k + 1)
        streak = 1

        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                streak += 1
            else:
                streak = 1

            if streak >= k:
                ans[i - k + 1] = nums[i]

        return ans      