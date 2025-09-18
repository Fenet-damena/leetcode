# Problem: All Divisions With the Highest Score of a Binary Array - https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        z = 0
        t1 = sum(nums)
        o = t1
        scores = []

        for i in range (len(nums)+1):
            score = z + o
            scores.append(score)

            if i < len(nums):
                if nums[i] == 0:
                   z += 1
                else:
                 o -=1
        m =max(scores)

        ans = [ i for i,v  in  enumerate(scores) if v == m]
        return ans

