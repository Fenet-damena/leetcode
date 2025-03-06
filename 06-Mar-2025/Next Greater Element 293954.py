# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        index =Counter()

        for num in nums2:
           
            while stack and stack[-1] < num:
                 poped = stack.pop()
                 index[poped] = num 
            stack.append(num)
        
        while stack:
            index[stack.pop()] = -1
        ans = [index[n] for n in nums1]
        return ans 