# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        m = len(nums)
       
        ans = []
        
        
        for i in range(1 << m):
            subset = []
            for j in range(m):
                if i &(1 << j):
                    
                    subset.append(nums[j])
           
            ans.append(subset)
         
        return ans