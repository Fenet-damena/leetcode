# Problem: Sum of All Subset XOR Totals - https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ans = 0

        def dfs(i, curr):
            if i == len(nums):
                self.ans += curr
                return
            dfs(i + 1, curr ^ nums[i])  # include nums[i]
            dfs(i + 1, curr)            # exclude nums[i]

        dfs(0, 0)
        return self.ans
        