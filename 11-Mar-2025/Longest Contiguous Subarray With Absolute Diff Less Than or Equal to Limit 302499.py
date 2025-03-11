# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_dq = deque()
        min_dq = deque()
        left = res = 0

        for right, num in enumerate(nums):
            while max_dq and num > max_dq[-1]:
                max_dq.pop()
            max_dq.append(num)

            while min_dq and num < min_dq[-1]:
                min_dq.pop()
            min_dq.append(num)

            while max_dq[0] - min_dq[0] > limit:
                if nums[left] == max_dq[0]:
                    max_dq.popleft()
                if nums[left] == min_dq[0]:
                    min_dq.popleft()
                left += 1

            res = max(res, right - left + 1)

        return res

