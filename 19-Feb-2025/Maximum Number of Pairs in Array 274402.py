# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        ans = [0,0]
        for key ,val in freq.items():
            ans[0]+=val//2
            ans[1]+=val%2
        return ans
            



        