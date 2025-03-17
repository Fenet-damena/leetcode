# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        l, r = 0, len(nums) - 1
        
        def rec(arr, l, r):
            if l == r:
                return arr[l]
            
            sl = nums[l] - rec(nums, l + 1, r)
            sr = nums[r] - rec(nums, l, r - 1)
            
            return max(sl, sr)
        
        return rec(nums, l, r) >= 0
