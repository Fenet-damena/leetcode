# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        c=Counter(nums)

        for k in c.keys():
            if c[k]>(len(nums)//2):
                return k
        
        
        