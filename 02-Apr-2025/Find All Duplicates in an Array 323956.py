# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        ans = []
        for k,v in freq.items():
            if v >1:
                ans.append(k)
        return ans

        