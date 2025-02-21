# Problem: Left-and-right-sum-differences - https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum = [0]*len(nums)
        rightsum = [0]*len(nums)

        for i in range(1,len(leftsum)):
            leftsum[i] = leftsum[i-1] + nums[i-1]
        for i in range(len(leftsum)-2,-1,-1):
            rightsum[i] = rightsum[i+1] + nums[i+1]

        ans = []

        for i in range(len(rightsum)):
            ans.append(abs(rightsum[i]-leftsum[i]))

        return ans  



        