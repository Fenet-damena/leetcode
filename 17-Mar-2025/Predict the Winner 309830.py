# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        score = 0
        left = 0
        right = len(nums) -1
        def recurse(arr,left,right):
            if left == right:
                return arr[left]

            scoreleft = nums[left] - recurse(nums,left + 1, right)

            scoreright = nums[right] - recurse(nums,left,right-1)

            return max(scoreleft,scoreright)
            
        return recurse(nums,left,right) >= 0


