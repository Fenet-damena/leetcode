# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(n):
            if n < 0:
                return 0
            l=0
            cur = 0
            ans = 0
            for r in range(len(nums)):
                cur += nums[r]
                while cur > n:
                    cur -= nums[l]
                    l +=1
                ans +=(r -l + 1)
            return ans
        return helper(goal)- helper(goal-1)