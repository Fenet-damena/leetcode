# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_s = float('inf')
        max_s = float('-inf')
        total = 0

        for i in nums:
            total += i
            min_s = min(min_s, total)
            max_s = max(max_s, total)
        return max(max_s - min_s,abs(max_s),abs(min_s))

        