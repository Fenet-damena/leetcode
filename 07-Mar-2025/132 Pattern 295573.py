# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        stack = []
        min_value = nums[0]

        for num in nums:

            while stack and  stack[-1][0] <= num:
                stack.pop()
            if stack and stack[-1][1] < num:
                return True
            stack.append([num, min_value])
            min_value = min(min_value, num)
        return False
            
           