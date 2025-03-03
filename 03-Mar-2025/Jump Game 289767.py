# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current = 0

        for i in range(len(nums)):
            if  current < i:
                return False
            current =  max(current, i+nums[i])
        return True
